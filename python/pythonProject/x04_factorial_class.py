class Factorial:
    def __init__(self, x):
        self.x = x

    def factorial(self):
        if self.x == 0:
            return 1
        else:
            return self.x * Factorial(self.x - 1).factorial()


input = int(input("Input the number: "))
fact = Factorial(input)
print(f"{input} factorial = {fact.factorial()}")


