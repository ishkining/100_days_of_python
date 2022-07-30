from bs4 import BeautifulSoup
import lxml
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response_empire = requests.get(URL)

data_empire = response_empire.text

soup = BeautifulSoup(data_empire, 'html.parser')

titles = [title.getText() for title in soup.select('h3.jsx-3523802742')]
titles = titles[::-1]

with open('movies.txt', 'w') as file:
    [file.write(f'{movie}\n') for movie in titles]


# response = requests.get('https://news.ycombinator.com/news')
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, 'html.parser')
# articles = soup.find_all(name='a', class_='titlelink')
# article_texts = []
# article_links = []
# for article_tag in articles:
#     article_texts.append(article_tag.getText())
#     article_links.append(article_tag.get('href'))
# article_upvotes = [int(score.getText().split()[0])for score in soup.find_all(name='span', class_='score')]
#
# print(article_texts)
# print(article_upvotes)
#
# print(article_texts[article_upvotes.index(max(article_upvotes))])

# with open("webiste.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'lxml')
