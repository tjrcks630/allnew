import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'

filename = '산불월별발생횟수.csv'
myframe = pd.read_csv(filename, encoding='utf-8')
# print(myframe)

column_name = '연도'  
myframe = myframe.set_index(keys=column_name)
print(myframe)

# plt.plot(kind='line', title='연도별 산불 현황', figsize=(10, 6), legend=True)

# filename = 'FireGrape01.png'
# plt.savefig(filename, dpi=400, bbox_inches='tight')
# print(filename + ' 파일이 저장되었습니다.')

# plt.show()











