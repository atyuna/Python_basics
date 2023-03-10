
class MyClass():

    def __init__(self):
        print("__init of class 1")
        self.prop_cl_1 = 10

    def method_1_class_1(self):
        print("method_1_class_1")

class MyClass2(MyClass):        #(inherit another class/or multiple classes)

    def __init__(self):
        super().__init__()
        print("__init of class 2")
        
    def method1_class2(self):
        print("method_1_class_2")

# obj1 = MyClass()
# obj1.method_1_class_1()

obj2 = MyClass2()
obj2.method1_class2()
