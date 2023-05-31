# 스포츠 기사 크롤링

import requests
from bs4 import BeautifulSoup as bs

from apps.resources.models import Article


def crawling_sports_news():
    sports_url = "https://sports.news.naver.com"

    sports_url_index = sports_url + "/index"

    response = requests.get(sports_url_index)
    soup = bs(response.text, "html.parser")

    ul = soup.find("ul", {"class": "today_list"})
    lis = ul.findAll("li")

    sports_news_list = []

    for li in lis:
        sports_news_list.append(sports_url + li.find("a")["href"])

    parsed_news = []

    for news in sports_news_list:
        response = requests.get(news)
        soup = bs(response.text, "html.parser")
        title = (
            soup.select(".content_area >.news_headline > .title")[0]
            .text.replace("\n", "")
            .replace("\t", "")
            .replace("\r", "")
        )
        content = (
            soup.select(".content_area > .news_end")[0]
            .text.replace("\n", "")
            .replace("\t", "")
            .replace("\r", "")
            .split("기사제공")[0]
        )
        url = news
        if len(content) > 500:
            parsed_news.append(
                {
                    "title": title,
                    "content": content,
                    "url": url,
                }
            )

    if len(content) > 500 & len(content) < 4000:
        for news in parsed_news:
            if Article.objects.filter(title=news["title"]).exists():
                continue
            else:
                Article.objects.create(
                    kind=Article.ArticleKindChoices.SPORTS,
                    title=news["title"],
                    content=news["content"],
                    url=news["url"],
                )

    # if len(parsed_news) > 0:
    #     Article.objects.bulk_create(
    #         [
    #             Article(
    #                 title=news["title"],
    #                 content=news["content"],
    #                 url=news["url"],
    #             )
    #             for news in parsed_news
    #         ]
    #     )
