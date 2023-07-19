import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    response = requests.get('https://docs.python.org/4/')
    soup = BeautifulSoup(response.text, features='lxml')
    print(soup.html.body.prettify())