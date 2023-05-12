from pandas import Series

myindex = ['강감찬', '이순신', '김유신', '광해군', '연산군', '을지문덕']
mylist = [50, 60, 40, 80, 70, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)
print('\ndType : ', type(myseries))

#1번째 항목을 100으로 변경
myseries[1] = 100

#2번째부터 4번째까지 999로 변경
myseries[2:4] = 999

#강감찬과 을지문덕을 30으로 변경
myseries[['강감찬', '을지문덕']] = 30

print('\n시리즈내용확인')
print(myseries)