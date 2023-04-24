from apscheduler.schedulers.background import BackgroundScheduler

# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# import asyncio


import datetime


def test():
    print(f"cron test 입니다. {datetime.datetime.today()}")


def cron_jobs():
    sched = BackgroundScheduler()  # django와는 다른 thread에서 돌아감
    # async_sched = AsyncIOScheduler()  # django와는 다른 thread에서 돌아감
    sched = BackgroundScheduler(timezone="Asia/Seoul")
    # sched.add_job(visitor_collector, "interval", seconds=60)
    # sched.add_job(telegram_command_handler, "interval", seconds=5)
    # sched.add_job(db_job_handler, "interval", seconds=10)
    # sched.add_job(XXXX, "cron", hour=4) # corn을 입력하면 매일 몇시 몇분에 실행할지 설정 할 수 있음
    # settings에서 TIME_ZONE = 'Asia/Seoul'로 세팅했으니 kst기준
    # sched.add_job(daily, "cron", args=[1], hour=4, minute=5)
    # sched.add_job(daily, "cron", args=[1], hour=17, minute=28, second=50)
    # sched.add_job(test, "interval", seconds=1)

    sched.start()


# https://apscheduler.readthedocs.io/en/3.x/

# nohup python manage.py runserver &
