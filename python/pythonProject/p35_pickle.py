import pickle


class SmartPhone(object):
    def __init__(self, brand, marker, price):
        self.brand = brand
        self.marker = marker
        self.price = price
    def __str__(self):
        return f'str : {self.brand} - {self.marker} - {self.price}'

object = SmartPhone("Iphone", "Apple", 10000)
f = open("test.pickle", "wb")
pickle.dump(object, f)
f.close()

f = open("test.pickle","rb")
object = pickle.load(f)
print(object)
f.close()
