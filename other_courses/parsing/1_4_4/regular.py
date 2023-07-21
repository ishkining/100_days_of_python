import re


addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.']


for address in addresses:
    # Напишите регулярное выражение.
    pattern = r'город.? (?P<city>\w+).*улиц.? (?P<street>\w+).*дом.? (?P<home>\d+).* квартир.? (?P<apartment>\d+)'

    address_match = re.search(pattern, address)
    # Распечатайте названия городов и улиц, номера домов и квартир
    # из обеих строк.
    city, street, home, apartment = address_match.groups()
    print(city, street, home, apartment)
