from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

mylist = [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운', '노천명','윤동주', '이옥사']

print(myindex)
print(mylist)
print('-' * 50)

myseries = Series(data=mylist, index=myindex)
mylim = [0, myseries.max() + 10]
myseries.plot(title = '금일 실적', kind = 'line', ylim = mylim,
              grid=False, rot=40, use_index=True)

filename = 'seriesGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+ 'save..')
plt.show()