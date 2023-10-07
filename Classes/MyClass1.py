
class myClass1:
    
    def __init__(self, cls1):
        print("__init__ of myClass1")
        self.prop_cls =10
        self.cls1 = cls1
        print(self.cls1)
        
    def method_1_class_1(self):
        print("method_1_class_1")    

class MyClass2(myClass1):

    def __init__(self, cl):
        super().__init__(cl)
        print("__init__ of myClass2")
    
    def method_1_class_2(self):
        print("method_1_class_2 of myClass")
   
   
        
# obj1 = myClass1()
# obj1.method_1_class_1()

obj2 = MyClass2('This is my argument')
obj2.method_1_class_2()
 
