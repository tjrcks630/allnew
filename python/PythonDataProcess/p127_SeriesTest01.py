from pandas import Series

mylist = [10, 40, 30, 20]
myseries = Series(data=mylist, index=['김유신', '이순신', '강감찬', '광해군'])

print('\nData Type')
print(type(myseries))

#index.name
myseries.index.name = '점수'
print('\nindex name of series')
print(myseries.index.name)

#.name
myseries.index.name = '학생들시험'
print('\nname of series')
print(myseries.name)

#index
print('\nname of index')
print(myseries.index)

#values
print('\nvalue of series')
print(myseries.values)

print('\nprint information of series')
print(myseries)

print('\nrepeat print')
for idx in myseries.index:
    print('Index : ' +idx + ', Values : ' + str(myseries[idx]))