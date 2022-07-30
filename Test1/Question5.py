#1
#default constructor
class Default:
 
    def __init__(self):
        self.default = "This is a default constructor"
 
    def print_default(self):
        print(self.default)

obj = Default()

obj.print_default()
#parameterized constructor
class Addition:
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
     
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
 
    def calculate(self):
        self.answer = self.first + self.second

obj = Addition(1000, 2000)
 
obj.calculate()
 
obj.display()

#2
#this is a class
class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width
    
    def rectangleArea(self):
        return self.length * self.width

    def rectanglePeremiter(self):
        return 2 * (self.length + self.width)

#this is an object
rect = Rectangle(3 , 4)

