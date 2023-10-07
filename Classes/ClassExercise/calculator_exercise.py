
# without the constractor
class BasicCalculator:
    
    def add(self, y, x):
        print("adding two numbers")
        return y + x

    def subtract(self, y, x):
        print("subtracing two numbers")
        return y - x

    def divide(self, y, x):
        print("dividing two numbers")
        return y / x
    
    def multiply(self, y, x):
        print("multiple two numbers")
        return y * x
        
# mycall = BasicCalculator()
# my_sum = mycall.add(2 ,2)
# print(my_sum)
# demostore.superqa.com


class BasicCalculator1:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        print("adding two numbers")
        return self.x + self.y

    def subtract(self):
        print("subtracing two numbers")
        return self.y - self.x

    def divide(self):
        print("dividing two numbers")
        return self.x / self.y
    
    def multiply(self):
        print("multiple two numbers")
        return self.x * self.y

        
mycall = BasicCalculator1(3 ,3)
my_sum = mycall.add()
my_sum1 = mycall.multiply()
print(my_sum)
print(my_sum1)