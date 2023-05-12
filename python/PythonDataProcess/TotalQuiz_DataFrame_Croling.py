import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
# 영화 데이터 Web에서 가져오기
url = "https://movie.daum.net/ranking/reservation"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
infos = soup.findAll('div', attrs={'class': 'thumb_cont'})

# Data 크롤링 및 저장
result = []
for info in infos:
    title = info.find('a', attrs={'class': 'link_txt'}).string
    grade = float(info.find('span', attrs={'class': 'txt_grade'}).string)
    rate = float(info.find('span', attrs={'class': 'txt_num'}).string.strip('%'))
    result.append((title, grade, rate))

# DataFrame으로 전환
mycolumn = ['제목', '평점', '예매율']
myframe = DataFrame(result, columns=mycolumn)

#DataFrame Index 지정 (set_index)
myframe = myframe.set_index('제목')

#예약률을 기준으로 데이터 프레임을 내림차순으로 정렬
myframe = myframe.sort_values(by='예매율', ascending=False)

#상위 10개 영화의 예매율 및 등급에 대한 가로 막대 그래프 만들기
myframe_top10 = myframe.iloc[:10][::-1]
ax = myframe_top10[['예매율', '평점']].plot(kind='barh', figsize=(10,6), color=['orange', 'b'])

# 그래프 만들기
ax.set_xlabel('예매율')
ax.set_ylabel('영화 제목')
ax.set_title('영화별 평점과 예매율')

# 인기있는 영화 제일 밑으로 내려줌
ax.invert_yaxis()

#그래프 보여주는 plt.show()
plt.show()

