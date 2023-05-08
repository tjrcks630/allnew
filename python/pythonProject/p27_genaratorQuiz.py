mynum = [1, 2, 3, 4, 5]


def square_number(nums):
    for mynum in nums:
        yield mynum ** 2
    return


num = square_number(mynum)
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())


for num in square_number(mynum):
    print(num)



