import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
site = response.text

soup = BeautifulSoup(site, "html.parser")

articles = soup.find_all(name="h3", class_="title")
article_titles = []

for article in articles:
    title = article.getText() + "\n"
    # title = f"{article.getText()}\n"
    article_titles.append(title)

article_titles.reverse()
print(article_titles)
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for film in article_titles:
        file.write(film)