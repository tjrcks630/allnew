def binary(number):
    if number in range(4,16):
        binary_list = []
        while number != 0:
            if number % 2 == 0:
                binary_list.insert(0, 0)
                number = number // 2
            else:
                binary_list.insert(0, 1)
                number = number // 2
        return  binary_list
    else:
        print('4~16 까지의 숫자를 입력하세요')
        return False


number = int(input('Input number 4 ~ 16: '))
binary_number = binary(number)
print(f'{number} binary number is :  {binary_number}')
















