# 스포츠 기사 크롤링

import requests
from bs4 import BeautifulSoup as bs

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
    desc = (
        soup.select(".content_area > .news_end")[0]
        .text.replace("\n", "")
        .replace("\t", "")
        .replace("\r", "")
        .split("기사제공")[0]
    )
    link = news
    parsed_news.append(
        {
            "title": title,
            "desc": desc,
            "link": link,
        }
    )


# 연예 기사 크롤링

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
    desc = (
        soup.find("div", {"id": "articeBody"})
        .text.replace("\n", "")
        .replace("\t", "")
        .replace("\r", "")
    )
    link = news
    parsed_news.append(
        {
            "title": title,
            "desc": desc,
            "link": link,
        }
    )
