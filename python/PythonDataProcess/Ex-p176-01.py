
from pandas import Series

mylist = [200, 300, 400, 100]
myseries = Series(data=mylist, index=['손오공', '저팔계', '사오정', '삼장법사'])

myseries.index.name = '실적현황'
print(myseries.index.name)

myseries.name = '직원 실적'
print(myseries.name)

for idx in myseries.index:
    print('색인 :' +idx ,' 값 : ' +str(myseries[idx]))