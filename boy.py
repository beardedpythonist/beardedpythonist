import requests
from bs4 import BeautifulSoup
import json
# ulr = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
heades = {
    'accept': 'Access-Control-Allow-Origin: *',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
#
# reg = requests.get(ulr, headers=heades)
# src = reg.text
# print(reg.text)
#
# with open('index2.html', 'w', encoding="utf-8") as file:
#     file.write(src)
#
# with open('index2.html', encoding="utf-8") as file:
#     src = file.read()
#
# all_categories = {}
# soup = BeautifulSoup(src, 'lxml')
# all_products = soup.find_all(class_="mzr-tc-group-item-href")
# for c in all_products:
#     c_text = c.text
#     c_href = 'https://health-diet.ru' + c.get('href')
#    # print(f'{c_text}, {c_href}')
#     all_categories[c_text] = c_href
# with open('all_categories.json', 'w') as file:
#     json.dump(all_categories, file, indent=4, ensure_ascii=False)   # непонятная строка!!!!!
#
with open('all_categories.json') as file:
    all_categories = json.load(file)

count = 0
for cat_name, cat_href in all_categories.items():
    if count == 0:
        rep = [",",":"," ","-"]
        for item in rep:
            if item in cat_name:
                cat_name = cat_name.replace(item, "_")
        print(cat_name)

        reg = requests.get(url=cat_href, headers=heades)
        src = reg.text

        with open(f'data/{count}_{cat_name}.html', 'w',  encoding="utf-8") as file:
            file.write(src)

        with open(f'data/{count}_{cat_name}.html', encoding="utf-8") as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')

        count += 1