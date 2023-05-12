import os
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame


url = 'https://movie.daum.net/ranking/reservation'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div' , attrs={'class' : 'thumb_cont'})
print('-' * 40)
print(infos)
print('-' * 40)

no = 0
#result변수를 빈 리스트를 만들어줌
result = []
for info in infos:
    no += 1
    #영화 제목
    # mytitle = info.find('a', attrs={'class':'link_txt'})
    # title = mytitle.string
    # print(title)

    #영화 평점
    # mygrade = info.find('span', attrs={'class': 'txt_grade'})
    # grade = mygrade.string
    # print(grade)

    #예매율
    # mynum = info.find('span', attrs={'class': 'txt_num'})
    # num = mynum.string
    # print(num)

    #개봉일
    # myrelease = info.find('span', attrs={'class': 'txt_info'})
    # release = myrelease.span.string
    # print(release)

    #모든 데이터를 result에 더해줌
    # result.append((no, title, grade, num, release))
    # print(result)