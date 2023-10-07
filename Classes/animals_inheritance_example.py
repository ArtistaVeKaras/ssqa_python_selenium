
class Animal:

    def __init__(self, color, food_type):
        print("I am a Animal")
        self.color = color
        self.food_type = food_type

    def move(self):
         print('Animal moves')

    def eat(self):
        print('animal eat')     
        print('this animal eats: {}'.format(self.food_type))
    
    def breath(self):
        print('Animal breath') 
        
class Dog(Animal):
    
    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.dog_breed = breed
        self.dog_name = name

    def bark(self):
        print("Woff....")    

    def security(self):
        print("I can use my dog as a security")

class Cat(Animal):
           
    def __init__(self, breed, name):
        self.cat_breed = breed
        self.cat_name = name

    def meaw(self):
        print("Meaw....")    

# obj of a dog
my_dog = Dog('Red','Meat','Buldog', 'Max')
print(my_dog.dog_breed)
print(my_dog.dog_name)
my_dog.eat()

# obj of a cat
# my_cat = Cat('Mutant', 'Tom')
# print(my_cat.cat_breed)
# print(my_cat.cat_name)


# this is just an example of change words that are the same
# this is just an example of change words that are the same
# this is just an example of change words that are the same
