# Импортируйте библиотеку BeautifulSoup.
from bs4 import BeautifulSoup
card_html = """
<div class="price sale" data-behavior="product-price" itemprop="offers"> 
  <meta itemprop="price" content="3490"> 
  <div class="title" data-behavior="price-title">
    <span class="text">Богатырские доспехи, шт.</span>
  </div>
  <div class="old-price">
    <span class="price" value="3490" data-behavior="price-old">3 490 рублей</span>
  </div>
  <div class="nameplate color-green" data-behavior="price-discount">Скидка 700 рублей</div> 
  <span class="price" value="2790" data-behavior="price-now">2 790 рублей</span>  
</div>
"""
# Сварите богатырский «суп» из HTML-кода.
soup = BeautifulSoup(card_html, features='lxml')

# Найдите в «супе» актуальную стоимость богатырских доспехов.
price_now = soup.find('span', attrs={'data-behavior': 'price-now'})

armor_cost = int(price_now.text.split()[0] + price_now.text.split()[1])
print(armor_cost)
