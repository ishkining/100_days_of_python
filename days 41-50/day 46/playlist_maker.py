import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100/2000-08-12/#'

response_billboard = requests.get(URL)
billboard_data = response_billboard.text

soup = BeautifulSoup(billboard_data, 'html.parser')

passer = False
labels_list = []
for text in soup.find_all(name='h3', id='title-of-a-story'):
    text = text.getText().replace('\n', '').replace('\t', '')
    if passer:
        labels_list.append(text)
        passer = False
    elif text == 'Imprint/Promotion Label:':
        passer = True

# EDITOR NOTE: Spotify doesnt work in Russian Federation, so I havent option and the program don't get 1st label
labels_list = labels_list[1:-1]
print(labels_list)


# USER_ID = 'ishkininking'
# URL = f'https://api.music.yandex.net/users/{USER_ID}/likes/tracks/add-multiple'
# URL_1 = 'api.music.yandex.net/account/status'
# params = {
#     'track-ids': 41284288,
# }
# response = requests.get(url=URL_1, headers=headers)
# print(response.text)