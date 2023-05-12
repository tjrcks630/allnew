from bs4 import BeautifulSoup
import numpy as np
from pandas import DataFrame


html = open('ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('body')
tbody = body.find('tbody')

names = ['황기태', '이재문', '이병은', '김남윤']

print('\n이름 과 성적 출력')
for tr in tbody.find_all('tr'):
    name = tr.find('td').text
    if name in names:
        html_score = tbody.find_all('td')[1].text
        css_score = tbody.find_all('td')[2].text
        print(f'{name}의 국어: {html_score}, 영어: {css_score}')
print('-' * 50)

mydata = [[80, 70], [95, 99], [85, 90], [50, 40]]
myindex = ['황기태', '이재문', '이병은', '김남윤']
mycolumns = ['국어' , '영어']

myframe = DataFrame(data=mydata, index=myindex, columns=mycolumns)
print(myframe)
print('-' * 50)