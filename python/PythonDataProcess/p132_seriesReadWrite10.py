from pandas import Series

myindex = ['용산구', '마포구', '영등포구', '서대문구', '광진구', '은평구', '서초구']
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = Series(data=mylist, index=myindex)
print(myseries)

#value read 해당 값의 정보를 찾는다 ex) 서대문구
print('\nread value')
print(myseries[['서대문구']])

#slicing 서대문구 부터 은평구까지의 데이터 조회
print('\nslicing')
print(myseries['서대문구' : '은평구'])

#data read 서대문구 와 서초구의 데이터를 조회
print('\ndata read')
print(myseries[['서대문구' , '서초구']])

#index read 2번째의 값을 불러온다.
print('\nread index')
print(myseries[[2]])

#index read 0, 2, 4
print('\nread index 0, 2, 4')
print(myseries[0:5:2])

#index read 1, 3, 5
print('\nread index 1, 3, 5')
print(myseries[[1, 3, 5]])

#slicing으로 해당 데이터만 불러옴
print('\nslicing')
print(myseries[3:6])

#2번째 항목에 있는 값 90으로 변경
myseries[2] = 90

#2번째부터 5번째까지 값 33으로 변경
myseries[2:5] = 33

#용산구 서대문구의 값을 55로 변경
myseries[['용산구', '서대문구']] = 55

#짝수행만 값을 77로 변경
myseries[0::2] = 80

