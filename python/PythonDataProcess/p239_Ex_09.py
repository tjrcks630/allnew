import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

slices = [1, 2, 3, 4, 5]
myindex = ['이상화', '한용운', '노천명', '윤동주', '이육사']
mycolors = ['blue', '#6AFF00', 'yellow', '#FF003C', 'green']
mylist = [30, 20, 40, 60, 50]

fig, ax = plt.subplots()

ax.pie(slices, labels=myindex, shadow=True,
        colors=mycolors, autopct='%1.2f%%', startangle=90, counterclock=False)

ax.legend(loc=4)

filename = 'pieGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()

