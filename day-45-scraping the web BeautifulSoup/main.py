from bs4 import BeautifulSoup
import requests
# before scraping check website root/robot.txt to get information what you can actually scrape and what you cant :)
response = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
# print((article_tag.getText()))
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.find(name="a").getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_article_index = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_article_index])
print(article_links[highest_article_index])


