import pandas as pd

#CSV 파일을 불러올 때
filename = 'seoul.csv'
df = pd.read_csv(filename)
print(df)

#CSV 파일 내의 해당 데이터 가져올때
result = df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동')]
print(result)

#서울특별시 강남구 신사동 의 단지명이 '삼지' 인 데이터만 출력
result = df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동') & (df['단지명'] == '삼지')]
print(result)

#도로명 주소로 Index를 만들고 싶을 때
newdf = df.set_index(keys=['도로명'])
print(newdf)

#도로명 주소가 동일로 인 Data를 출력
result = newdf.loc[['동일로']]
print(result)

#동일로인 Data의 갯 수를 파악
result = newdf.loc['동일로']
count = len(newdf.loc).loc['동일로'].count()
print(count)