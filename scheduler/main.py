from apscheduler.schedulers.background import BackgroundScheduler

# from apscheduler.schedulers.asyncio import AsyncIOScheduler

import datetime
from scheduler.fake_post import gpt_fake_post_by_article

from scheduler.gpt_obscured import gpt_obscure
from scheduler.article_summary import article_summary
from scheduler.news_crawling_entertain import crawling_entertain_news
from scheduler.news_crawling_sports import crawling_sports_news

sched = BackgroundScheduler(timezone="Asia/Seoul")
sched.start()


def test():
    print(f"cron test 입니다. {datetime.datetime.today()}")


def cron_jobs():
    # 매일 00시, 12시에 크롤링 시작
    sched.add_job(crawling_sports_news, "cron", hour="0, 12")
    sched.add_job(crawling_entertain_news, "cron", hour="0, 12")
    sched.add_job(gpt_obscure, "interval", seconds=1, id="gpt_obscure")
    sched.add_job(article_summary, "interval", seconds=1, id="article_summary")
    sched.add_job(
        gpt_fake_post_by_article, "interval", seconds=1, id="gpt_fake_post_by_article"
    )


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
