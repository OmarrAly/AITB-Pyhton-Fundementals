#Q1 output = False
#class list

#q2 pt1
def getnumbersfromfunc():
    x = y = z = 10
    return [x , y , z]
print(getnumbersfromfunc())

#pt2
def sum(num):
    def add(x):
        return num + x
    return add

#Q3 pt1
x = input("Enter a number to check if it is palindrome or not \n")

y = ""

for i in x:
    y = i + y

if (x == y):
    print("Yes")
else:
    print("No")

#pt2

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def merge_list(list1, list2):
    newlist = []
    
    for num in list1:
        if num % 2 != 0:
            newlist.append(num)
    
    for num in list2:
        if num % 2 == 0:
            newlist.append(num)
    return newlist

print("result list:", merge_list(list1, list2))

#pt3

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(3, 6)

#pt4

number = int(input ("Enter A number:\t "))             
print ("The Multiplication Table of: ", number)    
for i in range(1, 11):      
   print (number, 'x', i, '=', number * i)    

#pt5

x = input("Enter a word to reverse: \n")

y = ""

for i in x:
    y = i + y
print(y)

#pt6

for num in range(1, 100):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#pt7

for num in range(1,50):
    if num % 3 == 0 and num % 5 == 0:
        print ('FizzBuzz')
    elif num % 3 == 0:
        print ('Fizz')
    elif num % 5 == 0:
        print ('Buzz')

#pt8

x = ('omar', 'omar', 'omar')
result = all(x)
print(result)

#Fibonacci sequence

def fibonacci_of(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


print(fibonacci_of(n) for n in range(15))