import pandas as pd

#filename 변수에 csv 파일 불러옴
filename = 'memberInfo.csv'
df = pd.read_csv(filename)
print(df)

newdf01 = df.set_index(keys=['id'])
print(newdf01)

newdf02 = df.set_index(keys=['id'], drop=False)
print(newdf02)

df02 = pd.read_csv(filename, index_col='id')
print(df02)