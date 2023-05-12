from pandas import Series, DataFrame

#myseries1
myindex1 = ['성춘향', '이몽룡', '심봉사']
mylist1 = [40, 50, 60]

myseries1 = Series(data=mylist1, index=myindex1)

print('\n# 시리즈01')
print(myseries1)

#myseries2
myindex2 = ['성춘향', '이몽룡', '빵덕어멈']
mylist2 = [20, 40, 70]

myseries2 = Series(data=mylist2, index=myindex2)

print('\n# 시리즈02')
print(myseries2)

#두 시리즈 덧셈
print('\n# 두 시리즈 덧셈')
news = myseries1.add(myseries2, fill_value=10)
print(news)

#두 시리즈 뺄셈
print('\n# 두 시리즈 뺄셈')
news1 = myseries1.sub(myseries2, fill_value=30)
print(news1)