import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Canon-Rebel-T7-18-55mm-II/dp/B07C2Z21X5/ref=sr_1_1?qid=1659243416&rnid=502394&s=electronics&sr=1-1'
ANCHOR_PRICE = 480
headers = {
    'Accept-Language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,ru-RU;q=0.6,ru;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


amazon_response = requests.get(url=URL, headers=headers)
product_data = amazon_response.text

soup = BeautifulSoup(product_data, 'html.parser')
product_price = float(soup.find(name='span', class_='a-price-whole').getText())

if product_price < ANCHOR_PRICE:
    my_email = 'testertesttester2008@gmail.com'
    password = 'euotbkohfhwkewfq'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='detroil@gmail.com',
                            msg=f'Subject: Hello\n\nThe product that u wanted has price {product_price} now!')

