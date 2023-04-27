import requests
from bs4 import BeautifulSoup

# Список ссылок на сайты
urls = [
    'https://hobbygames.ru/search?query=',
    'https://wargame39.ru/search/?q=',
    'https://arma-models.ru/search/?q=',
    'https://edinorog.shop/search/?q='
]

# Список названий красок
paint_names = [
    'kraska-base-iron-hands-steel',
    'retributor-armour',
    'layer-white-scar',
    'layer-screaming-skull',
    'layer-fire-dragon-bright',
    'kraska-base-corax-white',
    'kraska-base-iron-warriors',
    'kraska-shade-nuln-oil-18-ml',
    'kraska-contrast-blood-angels-red'
]

# Создаем пустой список для хранения результатов
results = []

# Проходим по каждому сайту и каждой краске, получаем информацию о цене и наличии
for url in urls:
    prices = []
    for paint_name in paint_names:
        full_url = url + paint_name
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price_tag = soup.find('span', {'class': 'catalog-product-card__price__current'})
        if price_tag is not None:
            price = price_tag.text.strip()
        else:
            price = 'Нет в наличии'
        prices.append(price)
    results.append(prices)

# Выводим результаты в виде таблицы
for i, paint_name in enumerate(paint_names):
    print(paint_name.capitalize())
    for j, url in enumerate(urls):
        print(f'{j+1}. {url}{paint_name} - {results[j][i]}')
    print()
