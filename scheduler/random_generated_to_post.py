import datetime
from apps.resources.models.post_generated import PostGenerated


def random_generated_to_post():
    """
    생성된 애들중 랜덤하게 하나 post로 넘기기, 디버깅용
    """
    print("debug--- random_generated_to_post start")
    tmp = (
        PostGenerated.objects.filter(
            updated_at__gte=datetime.datetime.now() - datetime.timedelta(days=1)
        )
        .order_by("?")
        .first()
    )

    tmp.is_accepted = PostGenerated.PostChoices.ACCEPTED
    tmp.is_checked = True
    tmp.save()
