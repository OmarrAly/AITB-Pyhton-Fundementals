#1.1

from cmath import pi
from unicodedata import name

class Circle:
    def __init__(self , radius):
        self.radius = radius

    def getRaduis(self):
        return self.radius
    
    def setRaduis(self , radius):
        self.radius = radius
    
    def circleArea(self):
        return pow(self.radius , 2) * pi

    def circleCircumference(self):
        return 2 * pi * self.radius

    def displayCircleInfo(self):
        print(f"Circle : \n Radius = {self.radius} \n Area = {self.circleArea()} \n Circumfernce = {self.circleCircumference()}")


cir = Circle(4)
cir.displayCircleInfo()

#1.3

class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width
    
    def getlength(self):
        return self.length
    
    def setlength(self , length):
        self.length = length

    def getwidth(self):
        return self.width
    
    def setwidth(self , width):
        self.width = width
    
    def rectangleArea(self):
        return self.length * self.width

    def rectanglePeremiter(self):
        return 2 * (self.length + self.width)

    def displayRectangleInfo(self):
        print(f"Rectangle : \n length = {self.length} \n width = {self.width} \n Area = {self.rectangleArea()} \n Perimeter = {self.rectanglePeremiter()}")

rect = Rectangle(3 , 4)
rect.displayRectangleInfo()

#1.4

class Employee:
    def __init__(self , id , firstName, lastName , salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    
    def getid(self):
        return self.id

    def getfirstName(self):
        return self.firstName

    def getlastName(self):
        return self.lastName

    def getsalary(self):
        return self.salary
    
    def getid(self, id):
        self.id = id

    def setfirstName(self , firstName):
        self.firstName = firstName

    def setlastName(self , lastName):
        self.lastName = lastName

    def setsalary(self , salary):
        self.salary = salary
    
    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self):
        return (self.salary * 10/100) + self.salary
    
    def displayEmployeeInfo(self):
        print(f"Employee: \n ID = {self.id} \n firstName = {self.firstName} \n lastName = {self.lastName} \n salary = {self.salary} \n Name = {self.firstName} {self.lastName} \n AnnualSalary = {emp.getAnnualSalary()} \n raise = {emp.raiseSalary()} ") 

emp = Employee(8,'omar' , 'aly' , 1000)
emp.displayEmployeeInfo()

#1.6

class Account:
    def __init__(self , id , name , balance):
        self.id = id
        self.name = name
        self.balance = balance

    def getid(self):
        return self.id

    def getname(self):
        return self.name
    
    def getbalance(self):
        return self.balance

    def setid(self , id):
        self.id = id

    def setname(self , name):
        self.name = name
    
    def setbalance(self , balance):
        self.balance = balance
    
    def credit(self , balance , amount):
        amount += balance
        return balance
        
    def debit(self , amount , balance):
        if amount <= balance:
           balance = balance - amount
        else:
            print( "Amount exceeded balance")
        return balance

    def transferto(self , otheracc , amount , balance):
        if amount <= balance:
            otheracc += amount
        else:
            print("Amount exceeded balance")
        return balance
    
    def displayinfo(self):
        print(f"Account: \n ID = {self.id} \n name = {self.name} \n balance = {self.balance} \n credit = {acc.credit} \n debit = {acc.debit} \n transfer = {acc.transferto}")

acc = Account(8 , "omar aly" , 2000)
acc.displayinfo()

        
