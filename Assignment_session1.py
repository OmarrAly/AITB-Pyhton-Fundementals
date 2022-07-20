#1- Overall Appreciation App

grade = float(input('Enter Your Grade \n'))

if grade >= 85:
    print('excellent')
elif grade >= 75 and grade < 85: 
    print('very good')
elif grade >= 65 and grade < 75: 
    print('good')
elif grade >= 50 and grade < 65: 
    print('pass')
else:
    print('fail')

#2- FizzBuzz Game

num = int(input("Enter a number \n"))

if num % 3 == 0 and num % 5 == 0:
    print ('FizzBuzz')
elif num % 3 == 0:
    print ('Fizz')
elif num % 5 == 0:
    print ('Buzz')
else:
    print (str(num))

#3- Check Number is even or odd

numb = int(input ("Enter any number \n"))

if numb % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")

#4- check string is palindrome or not

x = input("Enter a word to check if it is palindrome or not \n")

y = ""

for i in x:
    y = i + y

if (x == y):
    print("Yes")
else:
    print("No")

#5- Calculate Rectangle Area and Perimeter

l=int(input("Enter length \n"))

w=int(input("Enter width \n"))

area=l*w

perimeter=2*(l+w)

print("Area : ",area)
print("Perimeter : ",perimeter)

