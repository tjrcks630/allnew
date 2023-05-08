class Binary:
    def __init__(self, number):
        if number in range(4,16):
            self.number = number
        else:
            print("4에서 16의 숫자만 입력하세요.")

    def binary(self):
        n = self.number

        if n in range(4,16):
            binary_list = []
            while n != 0:
                if n % 2 == 0:
                    binary_list.insert(0, 0)
                    n = n // 2
                else:
                    binary_list.insert(0, 1)
                    n = n // 2

            return binary_list
        else:
            print('4~16 까지의 숫자를 입력하세요')
            return False


number = int(input('Input random number 4 ~ 16 : '))
binary = Binary(number)
print(f'{binary.number}의 2진수는 {binary.binary()}입니다.')


















