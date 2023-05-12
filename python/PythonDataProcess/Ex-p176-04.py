import pandas as pd

sdata = {'색인': ['강감찬', '이순신', '김유신', '김구', '안중근'],
         '국어': [40, 60, 80, 50, 30],
         '영어': [55, 65, 75, 85, 60],
         '수학': [30, 40, 50, 60, 70]}

myframe = pd.DataFrame(data=sdata)
myframe.set_index('색인', inplace=True) # '색인' 열을 행 인덱스로 설정
print(myframe)

# 짝수 행만 읽어 보세요.
print('\n 짝수 행만 읽어 보세요.')
even_rows = myframe.iloc[::2]
print(even_rows)

# 이순신 행만 시리즈로 읽어 보세요.
print('\n 이순신 행만 시리즈로 읽어 보세요.')
lee_series = myframe.loc['이순신']
print(lee_series)

#강감찬의 영어 점수를 읽어 보세요.
print('\n 강감찬의 영어 점수를 읽어 보세요.')
kang_series = myframe.loc['강감찬', '영어']
print(kang_series)

#안중근과 강감찬의 국어/수학 점수를 읽어 보세요.
print('\n 안중근과 강감찬의 국어/수학 점수를 읽어 보세요.')
an_result = myframe.loc[['안중근','강감찬'], ['국어','수학']]
print(an_result)

#이순신과 강감찬의 영어 점수를 80으로 변경하세요
print('\n 이순신과 강감찬의 영어 점수를 80으로 변경하세요.')
myframe.loc[['안중근','강감찬'], ['영어']] = 80
print(myframe)

#이순신부터 김구까지 수학 점수를 100으로 변경하세요.
print('\n이순신부터 김구까지 수학 점수를 100으로 변경하세요.')
myframe.loc['이순신':'김구',['수학']] = 100
print(myframe)
