from pandas import Series

print('\nUnique, count, isin')
mylist = ['라일락', '코스모스', '코스모스','백일홍','코스모스','코스모스','코스모스','들장미','들장미','라일락','라일락' ]
myseries = Series(mylist)


#unique 중복을 제거한 모든 항목 보여줌
print('\nunique()')
myunipue = myseries.unique()
print(myunipue)

#value_count 값의 갯수를 새어줌
print('\nValue_count()')
print(myseries.value_counts())

#가지고 있는 Data 리스트안에 들장미 라일락이 맞는지 아닌지 출력
#True , False로 출력된다.
print('\nsin()')
mask = myseries.isin(['들장미', '라일락'])
print(mask)
print('-' * 50)

#
print(myseries[mask])
print('-' * 50)

print('\nfinished')