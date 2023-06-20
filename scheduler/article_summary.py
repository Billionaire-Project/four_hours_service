import time
import openai

from django.conf import settings
from apps.resources.models import Article, ArticleSummary

openai.api_key = settings.OPENAI_API_KEY


def article_summary() -> None:
    is_new = Article.objects.filter(
        is_summary=False,
    ).exists()

    if is_new:
        from scheduler.main import sched

        # network bound가 걸리니까 thead pause
        sched.get_job("article_summary").pause()

        articles = Article.objects.filter(
            is_summary=False,
        )

        print("debug--- summary start")
        for article in articles:
            sentence = article.content
            if len(sentence) < 4000:
                try:
                    article_summary = ArticleSummary()
                    article_summary.article = article
                    time_taken = 0

                    start = time.time()

                    print("debug--- sentence : ", sentence)
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "user",
                                "content": "다음 기사를 한국어로 요약해줘",
                            },
                            {"role": "user", "content": sentence},
                        ],
                    )

                    end = time.time()
                    time_taken += end - start
                    print("debug--- time_taken : ", time_taken)

                    article_summary.summary_content = completion.choices[
                        0
                    ].message.content
                    article_summary.time_taken = time_taken
                    article_summary.total_token = completion.usage.total_tokens
                    article_summary.save()

                    article.is_summary = True
                    article.save()
                except Exception as e:
                    print("debug--- error : ", e)
                    article.is_summary = True
                    article.save()
                    time.sleep(10)
                    continue
            else:
                article.is_summary = True
                article.save()

        print("debug--- summary end")
        sched.get_job("article_summary").resume()
