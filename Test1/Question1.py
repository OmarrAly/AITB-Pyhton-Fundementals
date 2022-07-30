#1-Lists and tuples are containers, which are used to store multiple data at the same time. The key difference is that Lists are mutable while Tuples are immutable.

#2- Break, continue  and pass are all used in loops.
#Break: Its used in a loop to terminate the loop and exit, when a condition is met.
#Continue: It causes a program to skip certain factors that come up within a loop, but then continue through the rest of the loop.
#Pass: It allows you to handle the condition without the loop being impacted in any way when an external condition is triggered.

#3- Self is used to represent an instance of a class

#4- A Python module, class, function, or method is documented with a string known as a "docstring" so that programmers may understand what it does.

#5- In multiple inheritance, the features of all the base classes are inherited into the derived class. 
#EX:
class Father():
    def Driving(self):
        print("Father Enjoys Driving")
class Mother():
    def Cooking(self):
        print("Mother Enjoys Cooking")
class Child(Father, Mother):
    def Learning(self):
        print("Child Learns skills from parents")
c = Child()
c.Driving()
c.Cooking()
c.Learning()
