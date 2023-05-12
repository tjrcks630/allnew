dictionary = {'김유신' : 50, '윤봉길' : 40, '김구' : 60}
print('dictionary list : ', dictionary)

for key in dictionary.keys():
    print(key)


for values in dictionary.values():
    print(values)


for key in dictionary.keys():
    print('{}의 나이는 {} 입니다.'.format(key, dictionary[key]))

for key,values in dictionary.items():
    print('{}의 나이는 {} 입니다.'.format(key, values))

findkey = '유관순'

if findkey in dictionary:
    print(findkey + '(은)는 존재합니다.')
else:
    print(findkey + '(은)는 존재하지 않습니다.')



result = dictionary.pop('김구')
print('After pop dictionary :' , dictionary)
print('pop value : ', result)


dictionary.clear()
print('dictionary list : ', dictionary)