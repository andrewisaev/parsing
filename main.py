import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/news/rubric/politics'
response= requests.get(url)
src=response.text

with open('index.html', 'w') as file:
    file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_a = soup.find_all(class_='mg-card__link')
for item in all_a:
    item_title = item.text
    item_href = item.get("href")
    print(f'{item_title}: {item_href}')
