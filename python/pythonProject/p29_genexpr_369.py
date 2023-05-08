numbers = (i for i in range(1,101))

for number in numbers:
    number = str(number)
    if '3' in number or '6' in number or '9' in number:
        print("👏" * number.count('3') + "👏" * number.count('6') + "👏" * number.count('9'))
    else:
        print(number)


# print(list(numbers))


