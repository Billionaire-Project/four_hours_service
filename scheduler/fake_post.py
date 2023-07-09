import time
import openai
from apps.resources.models import (
    ArticleSummary,
    PersonaPreset,
    PostGenerated,
)


def gpt_fake_post_by_article():
    """
    - 크롤링 된 기사 중 아직 사용되지 않은 기사들을 대상으로 가짜 포스트를 생성합니다.
    """

    is_new = ArticleSummary.objects.filter(is_used=False).exists()

    if is_new:
        from scheduler.main import sched

        sched.get_job("gpt_fake_post_by_article").pause()

        article_summarys = ArticleSummary.objects.filter(is_used=False)

        print("debug--- gpt_fake_post_by_article start")

        for article_summary in article_summarys:
            for _ in range(2):
                persona = (
                    PersonaPreset.objects.filter(
                        article_kind=article_summary.article.kind
                    )
                    .order_by("?")
                    .first()
                )

                prompt = f"""
                기사의 요약본을 읽고, 감상문을 200자 이내로 작성해주세요.
                - 기사 제목: {article_summary.article.title}
                - 기사 요약: {article_summary.summary_content}
                
                저는 당신이 SNS에 글을 게시하는 사람처럼 연기해주기를 바랍니다. 정보의 나열이 아니라, 그것을 보고 자신의 경험과 엮어서 말하는 것 처럼 글을 작성해 주세요.
                감정을 담백하는 것 처럼 연기해주세요. 작성자의 말투, 성격에 따라서 이모지 활용 빈도를 조절해 주세요. 작성자 개인의 욕망을 표현하는 것처럼 연기해주세요.
                자기를 최대한 표현하고 싶은 성향이 있는 사람 인 것 처럼 연기해주세요. 창의성, 다양성, 무작위성, 감성을 높이고 일관성을 낮춰주세요.

                작성자의 특징은 다음과 같습니다.
                - 직업: {persona.job}
                - 성별: {persona.gender}
                - 연령대: {persona.age}
                - 말투: {persona.tone}
                - 성격: {[i.content for i in persona.characteristic.all()]}
                """

                print(f"{article_summary.article.title} : {persona.name} 작성 시작")

                try:
                    start = time.time()
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        top_p=1,
                        temperature=1,
                        messages=[
                            {"role": "user", "content": prompt},
                        ],
                    )
                    end = time.time()
                    print(f"time taken: {end - start}")

                    article_summary.is_used = True
                    article_summary.save()

                    message = completion.choices[0].message.content

                    if message[0] == '"':
                        message = message.replace('"', "")

                    token = completion.usage.total_tokens

                    PostGenerated.objects.create(
                        content=message,
                        article=article_summary.article,
                        persona_preset=persona,
                        time_taken=end - start,
                        total_token=token,
                    )

                except Exception as e:
                    print(e)
                    time.sleep(10)
                    continue

        sched.get_job("gpt_fake_post_by_article").resume()
