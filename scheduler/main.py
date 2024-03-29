from apscheduler.schedulers.background import BackgroundScheduler

# from apscheduler.schedulers.asyncio import AsyncIOScheduler

from scheduler.fake_post import gpt_fake_post_by_article

from scheduler.gpt_obscured import gpt_obscure
from scheduler.article_summary import article_summary
from scheduler.news_crawling_entertain import crawling_entertain_news
from scheduler.news_crawling_sports import crawling_sports_news
from scheduler.post_generated_post import post_generatred_post
from scheduler.random_generated_to_post import random_generated_to_post

import os

ENTRY_PORT = int(os.environ.get("ENTRY_PORT", default=3030))

sched = BackgroundScheduler(timezone="Asia/Seoul")
sched.start()


def cron_jobs():
    # 매일 00시, 12시에 크롤링 시작
    sched.add_job(crawling_sports_news, "cron", hour="0, 12")
    sched.add_job(crawling_entertain_news, "cron", hour="0, 12")
    # sched.add_job(gpt_obscure, "interval", seconds=1, id="gpt_obscure")
    # sched.add_job(article_summary, "interval", seconds=1, id="article_summary")
    # sched.add_job(
    #     gpt_fake_post_by_article, "interval", seconds=1, id="gpt_fake_post_by_article"
    # )
    # sched.add_job(
    #     post_generatred_post, "interval", seconds=1, id="post_generatred_post"
    # )
    # if ENTRY_PORT == 3030:
    #     sched.add_job(
    #         random_generated_to_post,
    #         "cron",
    #         hour="0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22",
    #         id="random_generated_to_post",
    #     )


# sched = BackgroundScheduler()  # django와는 다른 thread에서 돌아감
# async_sched = AsyncIOScheduler(timezone="Asia/Seoul")  # django와는 다른 thread에서 돌아감
# sched = BackgroundScheduler(timezone="Asia/Seoul")
# async_sched.add_job(test, "cron", second=1)
# sched.add_job(visitor_collector, "interval", seconds=60)
# sched.add_job(telegram_command_handler, "interval", seconds=5)
# sched.add_job(db_job_handler, "interval", seconds=10)
# sched.add_job(XXXX, "cron", hour=4) # corn을 입력하면 매일 몇시 몇분에 실행할지 설정 할 수 있음
# settings에서 TIME_ZONE = 'Asia/Seoul'로 세팅했으니 kst기준
# sched.add_job(daily, "cron", args=[1], hour=4, minute=5)
# sched.add_job(daily, "cron", args=[1], hour=17, minute=28, second=50)
# sched.add_job(test, "interval", seconds=1, id="test")
# async_sched.start()
# pass
