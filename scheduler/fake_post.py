import time
import openai
from apps.resources.models import Persona
from apps.resources.models.article import Article
from apps.resources.models.persona_preset import PersonaPreset
from apps.resources.models.post_genetated import PostGenerated


def gpt_fake_post_by_article():
    """
    - 크롤링 된 기사 중 아직 사용되지 않은 기사들을 대상으로 가짜 포스트를 생성합니다.
    """
    articles = Article.objects.filter(is_used=False)

    for article in articles:
        for i in range(2):
            random_persona = PersonaPreset.objects.order_by("?").first()
            # 뉴스의 성격에 따라 작성자의 프로필을 따로 설정해야할듯?

            prompt = f"""
            아래와 같은 기사가 있습니다. 이 기사를 바탕으로 트위터에 게시할 글을 작성해주세요.
            - 기사 제목: {article.title}
            - 기사 내용: {article.content}
            작성자의 특징은 다음과 같습니다.
            - 직업: {random_persona.job}
            - 성별: {random_persona.gender}
            - 연령대: {random_persona.age}
            - 말투: {random_persona.tone}
            - 성격: {[i.content for i in random_persona.characteristic.all()]}
            """

            print(f"{article.title} : {random_persona.name} 작성 시작")

            try:
                start = time.time()
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                )
                end = time.time()
            except Exception as e:
                print(e)
                time.sleep(10)
                continue

        article.is_used = True
        article.save()

        message = completion.choices[0].message.content
        # message의 양 끝에 " "가 있다면, 제거합니다.
        if message[0] == '"' and message[-1] == '"':
            message = message[1:-1]

        token = completion.usage.total_tokens

        PostGenerated.objects.create(
            content=message,
            article=article,
            persona_preset=random_persona,
            time_taken=end - start,
            total_token=token,
        )
