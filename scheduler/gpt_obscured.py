import time
import openai

from django.conf import settings
from apps.posts.models import Post, PostObscured

# from scheduler.main import sched

openai.api_key = settings.OPENAI_API_KEY


def gpt_obscure() -> None:
    is_new = Post.objects.filter(
        is_obscured=False,
        is_deleted=False,
    ).exists()

    if is_new:
        from scheduler.main import sched
        from scheduler.nltk_tokenize import count_meaningful_words

        # network bound가 걸리니까 thead pause
        sched.get_job("gpt_obscure").pause()

        posts = Post.objects.filter(
            is_obscured=False,
            is_deleted=False,
        )

        print("debug--- gpt_obscure start")
        for post in posts:
            post_obscured = PostObscured()
            post_obscured.user = post.user
            post_obscured.post = post
            time_taken = 0
            total_token = 0

            if count_meaningful_words(post.content) >= 5:
                sentence = post.content
                print("debug--- sentence : ", sentence)
                try:
                    start = time.time()
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        # model="gpt-4",
                        messages=[
                            {
                                "role": "user",
                                "content": "다음 문장의 핵심 단어만 출력해줘",
                                # "content": "다음 문장의 핵심 단어만 출력해줘, 불가능하다면 false만 출력해줘",
                                # 이 조건으로 출력이 항상 같지 않음, 세밀한 조정이 필요할듯
                            },
                            {"role": "user", "content": sentence},
                        ],
                    )
                    end = time.time()
                    time_taken = round(end - start, 2)
                    total_token = completion.usage.total_tokens
                    result = completion.choices[0].message.content
                    print("debug--- result : ", result)

                    if not result.__contains__("false"):  # 변경 가능
                        is_failed = False
                        obscured_words = result.split(", ")
                        print("debug--- obscured_words : ", obscured_words)
                        obscured_content = sentence
                        for word in obscured_words:
                            # gpt가 이상한 단어를 뽑아줬을 경우 예외처리
                            if result.__contain__(word):
                                obscured_content = obscured_content.replace(
                                    word, "_" * len(word)
                                )
                            else:
                                is_failed = True
                                break
                        print("debug--- obscured_content : ", obscured_content)
                        post_obscured.obscured_words = obscured_words
                        post_obscured.obscured_content = obscured_content
                        post_obscured.is_failed = is_failed
                        post_obscured.time_taken = time_taken
                        post_obscured.total_token = total_token
                except:
                    time.sleep(10)
                    continue

                else:
                    is_failed = True

            else:
                is_failed = True

            if is_failed:
                post_obscured.obscured_words = ""
                post_obscured.obscured_content = ""
                post_obscured.is_failed = is_failed
                post_obscured.time_taken = time_taken
                post_obscured.total_token = total_token

            post_obscured.save()
            post.is_obscured = True
            post.save()
            print("debug--- gpt_obscure end")

        # 마무리 후 resume
        sched.get_job("gpt_obscure").resume()
