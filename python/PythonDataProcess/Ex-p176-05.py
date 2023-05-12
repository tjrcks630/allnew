from pandas import Series, DataFrame
import numpy as np

# myseries
myindex = ['윤봉길', '김유신', '신사임당']
mylist = [30, 40, 50]
index = {'색인': myindex}
columns = {'값': mylist}
myseries = Series(data=mylist, index=myindex)
print('\n myseries')

print(myseries)

#myframe
myindex = ['윤봉길', '김유신', '이순신']
mycolumns = ['용산구','마포구','서대문구']
mylist = list(3 * onedata for onedata in range(1,10))


myframe = DataFrame(np.reshape(np.array(mylist),(3,3)),
index = myindex,
columns = mycolumns)
print('\n myframe')
print(myframe)

#myframe2
myindex2 = ['윤봉길', '김유신', '이완용']
mycolumns2 = ['용산구','마포구','은평구']
mylist = list(5 * onedata for onedata in range(1,10))

myframe2 = DataFrame(np.reshape(np.array(mylist),(3,3)),
index = myindex2,
columns = mycolumns2)
print('\n myframe2')
print(myframe2)

#DataFrame + Series
print('\n ataFrame + Series')

dase = myframe.add(myseries, axis = 0)
print(dase)

#DataFrame + DataFrame
print('\n DataFrame + DataFrame')
dada = myframe.add(myframe2, fill_value = 20)
print(dada)

#DataFrame - DataFrame
print('\n DataFrame - DataFrame')
dada = myframe.sub(myframe2, fill_value = 20)
print(dada)