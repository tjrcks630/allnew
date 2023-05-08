#!/usr/bin/env python

numbers = [0,1,2,3]
names = ["Kim", "Lee", "Park", "Choi"]
print(numbers[0])
print(names[2:])
print(numbers[-1])
print(numbers + names)


names.append("Moon")
print(names)
#append는 리스트 가장 뒤에 추가됨

names.insert(1, "Kang")
print(names)
#insert는 추가하려는 대상의 위치를 지정해줘야함
#예시의 경우에 1로 위치를 지정

empty = []
print(empty)

#delete
del names[1]
print(names)

#remove
names.remove("Moon")
print(names)

# pop
value = names.pop()
print(value)

#pop
value = names.pop(1)
print(value)


#extend
numbers.extend([4, 5, 6])
print(numbers)


#numbers에 4개 몇개 있는지 확인
print(numbers.count(4))

#sort
numbers.sort()
print(numbers)

#reverse 반대로 뒤집음
numbers.reverse()
print(numbers)

#clear = 리스트 내용을 모두 없앤다.
numbers.clear()
print(numbers)