tuple01 = (10, 20, 30)
tuple02 = tuple01 + (40, )

print('print Tuple : ', tuple01)


tuple02 = 10, 20, 30, 40

mylist = [10, 20, 30, 40]
tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print("Component equal")
else:
    print("Component not equal")

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
tuple06 = tuple04 + tuple05
print(tuple06)

tuple07 = tuple04 * 3
print(tuple07)


a, b = (11, 22)
a, b = b, a

print('a =', a, 'b =', b)
