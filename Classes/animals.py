class Animal:
    # pass

    def __init__(self, color, food_type):
        print("I am a Animal")
        self.color = color
        self.food_type = food_type

    def move(self):
         print('animal moves')

    def eat(self):
        print('animal eat')     
        print('this animal eats: {}'.format(self.food_type))
    
    def breath(self):
        print('animal breath')    


my_animal = Animal('red', 'beef')       
print(f"color of animal 1: {my_animal.color}")
print(f"food type of animal 1: {my_animal.food_type}")
print(my_animal)
my_animal.move()
my_animal.eat()