from apps.resources.models import PostGenerated
from apps.posts.models import Post
from apps.users.models import User


def post_generatred_post():
    """
    생성된 기사 중 is_accepted가 ACCEPTED이고 is_posted가 false인 기사를 post에 저장
    """

    is_new = PostGenerated.objects.filter(
        is_accepted=PostGenerated.PostChoices.ACCEPTED, is_posted=False
    ).exists()

    if is_new:
        from scheduler.main import sched

        sched.get_job("post_generatred_post").pause()

        post_generateds = PostGenerated.objects.filter(
            is_accepted=PostGenerated.PostChoices.ACCEPTED, is_posted=False
        )

        print("debug--- post_generatred_post start")

        for post_generated in post_generateds:
            post = Post()
            user = User.objects.get(id=1)
            post.user = user
            post.content = post_generated.content
            post.generated_post = post_generated
            post.save()

            post_generated.is_posted = True
            post_generated.save()

        sched.get_job("post_generatred_post").resume()
