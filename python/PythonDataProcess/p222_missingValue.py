import numpy as np
import pandas as pd
from pandas import Series

filename = "excel02.csv"

print("\n 누락 된 데이터 샘플 원본 데이터")
myframe = pd.read_csv(filename, index_col='이름')
print(myframe)

print("\n fillna() Method 이용, 출력할때만 결과를 바꾼다.")
print(myframe.fillna(0, inplace=False))

print("\n# inplace = False이므로 원본 변동은 없다.")
print(myframe)

print("\n# inplace = True 일 경우 원본 변동한다.")
myframe.fillna(0, inplace=True)
print(myframe)

print('\n 누락된 데이터 원본 ')
myframe.loc[['강감찬','홍길동'],['국어','영어']] = np.nan
myframe.loc[['박영희','김철수'],['수학']] = np.nan
print(myframe)

print('\n# 임의의 값을 다른 값으로 치환')
print('\n# 국어 , 영어 , 수학 칼럼의 NaN 값들을 아래의 값으로 변경')
mydict = {'국어' : 15, '영어' : 25, '수학' : 35}
myframe.fillna(mydict, inplace=True)

#값이 바뀌는지 확인
print(myframe)
print('-' * 40)


print('\n 누락된 데이터 원본 Data 다른 방식으로 생성 ')
myframe.loc[['박영희'],['국어']] = np.nan
myframe.loc[['홍길동'],['영어']] = np.nan
myframe.loc[['김철수'],['수학']] = np.nan

print(myframe)
print('-' * 40)

print('\n# 국어 , 영어 , 수학 칼럼의 다른 방식으로 변경')
mydict = {'국어' : np.ceil(myframe['국어'].mean()),
          '영어' : np.ceil(myframe['영어'].mean()),
          '수학' : np.ceil(myframe['수학'].mean())}

myframe.fillna(mydict, inplace=True)

print(myframe)
print('-' * 40)