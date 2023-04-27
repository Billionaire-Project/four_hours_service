import openai
from apps.posts.models import Post, PostObscured


def check_new_post() -> bool:
    """Check new post"""
    if Post.objects.filter(is_obscured=False).exists():
        return True
    return False


async def gpt_obscure():
    is_new = check_new_post()

    # if is_new:

    #     completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     # model="gpt-4",
    #     messages=[
    #         {"role": "user", "content": "다음 문장의 핵심 단어만 출력해줘 불가능하다면 false를 출력해줘"},
    #         {"role": "user", "content": sentence}
    #     ]
    #     )
