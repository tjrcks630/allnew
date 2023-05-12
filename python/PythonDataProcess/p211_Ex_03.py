import numpy as np
import pandas as pd
from pandas import Series

filename = "과일매출현황.csv"

print("\n #원본 데이터 프레임")
df = pd.read_csv(filename)
print(df)

print("\n#누락데이터 채워 넣기")
mydict = {'구입액' : 50 , '수입량' : 20}
df.fillna(mydict, inplace=True)
print(df)

print("\n#구입액과 수입량의 각 소계")
print(df[['구입액', '수입량']].sum())

print("\n#과일별 소계")
print(df.loc[:, '사과':'포도'].sum(axis=1))

print("\n#구입액과 수입량의 평균")
print(df[['구입액', '수입량']].mean(axis=1, skipna=True))

print("\n#과일별 평균")
print(df.loc[:, '사과':'포도'].mean(skipna=True))



