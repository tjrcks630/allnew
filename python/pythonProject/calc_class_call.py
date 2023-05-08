import calc_class

a = int(input('Input first number : '))
b = int(input('Input second number : '))

my = calc_class.Calc(a, b)

print(f'{a}  + {b} = {my.add()}')
print(f'{a}  - {b} = {my.sub()}')


## class_animal.py

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move~")
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('woof-woof')

class Duck(Animal):
    def speak(self):
        print('quack-quack')