#1
import string 
import random

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
digits = list(string.digits)

def generatePassword():
    
    passwordLength = int(input('Enter password length: '))
            
    password = []
    random.shuffle(uppercase)
    random.shuffle(lowercase)   
    random.shuffle(digits)
    
    for i in range(round(passwordLength * .4)):
        password.append(uppercase[i])

    for i in range(round(passwordLength * .3)):
        password.append(lowercase[i])

    for i in range(round(passwordLength * .3)):
        password.append(digits[i])

    

    password = "".join(password[0:])

    print(f"Your password is : \n  {password}")

generatePassword()