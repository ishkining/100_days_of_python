import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

import re

BASE_DIR = Path(__file__).parent

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
# Здесь весь уже написанный код.
if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    table_tag = soup.find('table')
    # Добавьте команду получения нужного тега.
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    pdf_a4_link = pdf_a4_tag['href']
    # Получите полную ссылку с помощью функции urljoin.
    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)

    filename = archive_url.split('/')[-1]

    # Сформируйте путь до директории downloads.
    downloads_dir = BASE_DIR / 'downloads'
    # Создайте директорию.
    downloads_dir.mkdir(exist_ok=True)
    # Получите путь до архива, объединив имя файла с директорией.
    archive_path = downloads_dir / filename

    # Загрузка архива по ссылке.
    response = session.get(archive_url)

    # В бинарном режиме открывается файл на запись по указанному пути.
    with open(archive_path, 'wb') as file:
        # Полученный ответ записывается в файл.
        file.write(response.content)