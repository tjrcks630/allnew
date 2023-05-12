import pandas as pd

filename = 'data02.csv'

df = pd.read_csv(filename, header=None, names=['이름', '학년', '국어', '영어', '수학'])
df = df.set_index(keys = ['이름', '학년', '국어', '영어'])
#수학을 넣으면 출력 이상하게 나옴
print(df)


