import re

from bs4 import BeautifulSoup

with open('index.html', encoding='utf-8') as file:
    q = file.read()
# print(q)
soup = BeautifulSoup(q, 'lxml')
# # print(soup.title)
# # print(soup.text)
# page1 = soup.find('h1')
#
# page_all = soup.findAll('div')
#
# user = soup.find('div', class_='user__name')
# print(user.text.strip())
# # вторй способсо словарем
# user = soup.find(('div', {'class': "user__name"})).find('span')
# print(user)
#
# span_info = soup.find(class_='user__info').findAll('span')
#
# for c in span_info:
#     print(c.text)

# find_social = soup.find(class_="social__networks").find('ul').findAll('a')
# print(find_social)
# for c in find_social:
#     print(c.get('href'))

findtext = soup.find('a', string=re.compile('Twitter'))
print(findtext)
