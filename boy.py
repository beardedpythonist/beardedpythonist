import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv
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
iteration_count = int(len(all_categories) - 1)

print(f' всего итарций {iteration_count}')
count = 0
for cat_name, cat_href in all_categories.items():

    rep = [",",":"," ","-"]
    for item in rep:
        if item in cat_name:
            cat_name = cat_name.replace(item, "_")

    reg = requests.get(url=cat_href, headers=heades)
    src = reg.text

    with open(f'data/{count}_{cat_name}.html', 'w',  encoding="utf-8") as file:
        file.write(src)

    with open(f'data/{count}_{cat_name}.html', encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    #  проверка страницы на наличие таблицы

    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue



    table_head = soup.find(class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tr').find_all('th')
    product  = table_head[0].text
    colories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbo  = table_head[4].text

    with open(f'data/{count}_{cat_name}.csv',  'w',  encoding="utf-8") as file:
        writer =  csv.writer(file)
        writer.writerow(
            (product, colories,
             proteins, fats, carbo)
        )
        # собираем данные проуктов
        product_data = soup.find(class_='uk-table mzr-tc-group-table '
                                        'uk-table-hover uk-table-striped uk-table-condensed').find('tbody').findAll('tr')
        for item in product_data:
            produts_tds = item.find_all('td')
            title = produts_tds[0].text
            colories = produts_tds[1].text
            proteins = produts_tds[2].text
            fats = produts_tds[3].text
            carbo = produts_tds[4].text

            with open(f'data/{count}_{cat_name}.csv', 'a', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (title, colories,
                     proteins, fats, carbo)
                )
    count += 1
    print(f' # итарция {count} ,  {cat_name} записан')
    iteration_count = iteration_count - 1
    if iteration_count == 0:
        print('работа завершена')
        break
    print(f' осталось итераций {iteration_count}')
    sleep(random.randrange(2,4))

