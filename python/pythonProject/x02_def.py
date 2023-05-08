import random

def findMax(data):

    # max_val = max(data)
    # print(data)
    # print(f'Max value is: {max_val}')
    # return max_val

    max = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return max

data = random.sample(range(1,101),10)
print(data)
print(f'Max value is : {findMax(data)}')

