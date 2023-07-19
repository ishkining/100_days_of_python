import requests
import requests_cache

# Импортируйте функцию для вывода прогресс-бара.
import requests
from tqdm import tqdm

DELAYED_URL = 'http://httpbin.org/delay/3'

if __name__ == '__main__':
    # Допишите к циклу прогресс-бар, дайте ему название "Загрузка с сервера".
    for i in tqdm(range(3), desc='Loading from server'):
        # Загрузка веб-страницы с сервера.
        requests.get(DELAYED_URL)

    # Сессия для работы с кешированной загрузкой.
    session = requests_cache.CachedSession()
    # Очистка кеша, чтобы каждый новый запуск программы
    # не зависел от предыдущего.
    session.cache.clear()

    # Допишите к циклу прогресс-бар, дайте ему название "Загрузка из кеша".
    for i in tqdm(range(3), desc='Loading from cache'):
        # Загрузка веб-страницы через кеширующую сессию.
        session.get(DELAYED_URL)