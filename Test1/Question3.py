#1
def is_vowel(letter):
    if letter in 'aeiouAEIOU':
        return True
    else:
        return False
        
def count_vowels():
    count = 0
    string = input('Enter a text: ')
    for i in string:
        if(is_vowel(i)):
            count += 1

    print('Number of vowels are', count)

count_vowels()

#2
def recurSum(n):
    if n <= 1:
        return n
    else:
        return n + recurSum(n - 1)

print(recurSum(5))

#3
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, 10):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

#4
dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in dict.values():
    print('200 present in a dict')

#5
from cmath import pi
from turtle import circle
from unicodedata import name

class Circle:
    def __init__(self , radius , color):
        self.radius = radius
        self.color = color

    def getRaduis(self):
        return self.radius

    def getcolor(self):
        return self.color

    def getArea(self):
        return pow(self.radius , 2) * pi
    
    def setRaduis(self , radius):
        self.radius = radius
    
    def setcolor(self, color):
        self.color = color

    def displayCircleInfo(self):
        print(f"Circle : \n Radius = {self.radius} \n Color = {self.color} \n Area = {self.getArea()}")

class cylinder(Circle):
    def __init__(self , radius, color , height):
        super().__init__(radius , color)
        self.height = height

    def getheight(self):
        return self.height
    
    def setheight(self, height):
        self.height = height
    
    def getvolume(self):
        return int(pi) * pow(self.radius , 2) * self.height
    
    def displayCylinderInfo(self):
        print(f"Cylinder : \n Radius = {self.radius} \n Height = {self.height} \n Volume = {self.getvolume()}")
    
cir = Circle(4, 'red')
cir.displayCircleInfo()
cyl = cylinder(4 , 'blue', 8 )
cyl.displayCylinderInfo()

    


