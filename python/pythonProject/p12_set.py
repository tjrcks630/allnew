even = set([0, 2, 4, 6, 8])
print(even)

hello = set("Hello")
print(hello)

s= even | hello
print(s)

p = even & hello
print(p)

even.add(10)
print(even)

even.add(10)
print(even)

hello.remove('e')
print(hello)


s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

#intersection 교집합
print(s1.intersection(s2))

#union 합집합
print(s1.union(s2))
print(s1 | s2)

#difference 차집합
print(s1.difference(s2))
print(s2.difference(s1))


s3 = {1,2,3,4,5}

if s1 == s2:
    print("s1, s2 is same...")
else:
    print("s1, s3 is not same...")


s4 = {6,7,8,9,10}

if s1.isdisjoint(s2):
    print("s1,s2 is same...")

else:
    print("s1, s2 is not same...")


s5 = {4,5}

s = {1,2,3}
print(f'set : {s}')

s.update({'a', 'b', 'c'})
print(f'set : {s}')

s.update([11,12,13])
print(f'set : {s}')


print(f'set.pop() : {s.pop()}')

s.clear()
print(f'set : {s}')

s = {'a','b', 'c'}

if 'a' in s:
    print('a is Exit')
else:
    print('a is not Exist')

if 'z' in s:
    print('z is Exist')
else:
    print('z is not Exist')

print(f'length of set " {len(s)}')
