wordInfo = {'세탁기' : 50, '선풍기' : 30, '청소기' : 40}

#Key값을 받아서 Value에 의한 크기 순으로 정렬
myxticks = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(myxticks)


revers_key = sorted(wordInfo.keys(), reverse=True)
print(revers_key)