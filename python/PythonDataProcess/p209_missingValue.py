import numpy as np
import pandas as pd
from pandas import DataFrame,Series

#np.nan을 이용한 NaN처리
print('\n#시리즈의 누락 데이터 처리')
print('#원본 시리즈')
myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)

#isnull을 이용해서 NaN일 때 True를 출력한다.
print('\n# isnull() 함수의 : NaN이면 True')
print(myseries.isnull())

#notnull을 이용해서 NaN이 아니면 True를 출력한다.
print('\n# notnull() 함수의 : NaN이 아니면 True')
print(myseries.notnull())

#notnull 이 참인 항목만 출력
print('\n# notnull 이 참인 항목만 출력')
print(myseries[myseries.notnull()])

#dropna로 이용 누락 데이터를 처리한다.
print('\n# dropna로 이용 누락 데이터를 처리한다.')
print(myseries.dropna())


filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름',
                      encoding='utf-8')
print(myframe)

print('\n# dropna() 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0)
print(cleaned)

print('\n# how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='all')
print(cleaned)

print('\n# how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='any')
print(cleaned)

print('\n# [영어] 칼럼에 NaN을 제거')
print(myframe.dropna(subset=['영어']))

print('\n# 칼럼 기준, how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='all')
print(cleaned)

print('\n# 칼럼 기준, how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='any')
print(cleaned)

#Before랑 After 비교
print('\n## before : ')
print(myframe)
myframe.loc[['강감찬','홍길동'], ['국어']] = np.nan
print('\n## after : ')
print(myframe)

#아예 세로로 NaN인 모든 것 Data 없어진 것 확인 된다.
print(myframe.dropna(axis=1, how="all"))


print('\n## thresh option')
print(myframe.dropna(axis=1, thresh=2))