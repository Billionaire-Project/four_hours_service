# 스포츠 기사 크롤링

import requests
from bs4 import BeautifulSoup as bs

from apps.resources.models import Article


def crawling_entertain_news():
    entertain_url = "https://entertain.naver.com"

    entertain_url_home = entertain_url + "/home"

    response = requests.get(entertain_url_home)
    soup = bs(response.text, "html.parser")

    ranking = soup.find("div", {"class": "rank_lst"})
    lis = ranking.findAll("li")

    entertain_news_list = []

    for li in lis:
        entertain_news_list.append(entertain_url + li.find("a")["href"])

    parsed_news = []

    for news in entertain_news_list:
        response = requests.get(news)
        soup = bs(response.text, "html.parser")
        title = (
            soup.select(".end_tit")[0]
            .text.replace("\n", "")
            .replace("\t", "")
            .replace("\r", "")
        )
        content = (
            soup.find("div", {"id": "articeBody"})
            .text.replace("\n", "")
            .replace("\t", "")
            .replace("\r", "")
        )
        url = news
        parsed_news.append(
            {
                "title": title,
                "content": content,
                "url": url,
            }
        )

    if len(parsed_news) > 0:
        for news in parsed_news:
            if Article.objects.filter(title=news["title"]).exists():
                continue
            else:
                Article.objects.create(
                    kind=Article.ArticleKindChoices.ENTERTAINMENT,
                    title=news["title"],
                    content=news["content"],
                    url=news["url"],
                )
