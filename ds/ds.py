import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd

url = 'http://books.toscrape.com/'
response = requests.get(url)
if response.status_code == 200:
    print("Страница успешно загружена!")
else:
    print(f"Ошибка! Код: {response.status_code}")
    exit() 
soup = BeautifulSoup(response.text, 'lxml')
books = soup.find_all('article', class_='product_pod')
books_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating_class = book.find('p', class_='star-rating')['class']
    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    rating = rating_map.get(rating_class[1], 'N/A')
    link = url + book.h3.a['href']

    books_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating,
        'Link': link
    })
df = pd.DataFrame(books_data)
print(df.head()) 
df.to_csv(r'C:\Users\Anna\OneDrive\Desktop\Учёба Бауманка\2 курс\Пяп\дз\books_dataset.csv', index=False, encoding='utf-8')
print("Датасет успешно сохранен в файл 'books_dataset.csv'")
# 3. ПРОСТОЙ АНАЛИЗ ДАННЫХ
print("\n=== ПРОСТОЙ АНАЛИЗ ===")
rating_names = {1: '★', 2: '★★', 3: '★★★', 4: '★★★★', 5: '★★★★★'}

print("\nКоличество книг по рейтингам:")
rating_counts = df['Rating'].value_counts().sort_index()
for rating, count in rating_counts.items():
    stars = rating_names.get(rating, str(rating))
    print(f"{stars}: {count} книг")

print(f"\n--- АНАЛИЗ ЦЕН ---")
print(f"Всего книг: {len(df)}")
# Преобразуем Price из строк в числа (убираем £)
df['Price'] = df['Price'].str.replace('Â£', '').astype(float)
# Теперь можно считать
print(f"Общая стоимость: £{df['Price'].sum():.2f}")
print(f"Средняя цена: £{df['Price'].mean():.2f}")
print(f"Самая дорогая: £{df['Price'].max():.2f}")
print(f"Самая дешевая: £{df['Price'].min():.2f}")

print("\n=== АНАЛИЗ ЗАВЕРШЕН ===")