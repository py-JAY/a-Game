import random as rad;

def check_upper(): #checks for value validity
    while True:
        m = input("Enter a upper value: ")
        if m.isdigit():
            n=int(m)
            break
        else:
            print("Enter a number!!")
    return n

def check_lower(): # does the same but or lower
    while True:
        c = input("Enter your lower value: ")
        if c.isdigit():
            d=int(c)
            break
        else:
            print("Enter a number!!")
    return d

def take_input(): #takes input from user and sends it a variables
    a=check_lower()
    b=check_upper()
    return a,b

def check_guess(): #checks the value for guess
    while True:
        k = input("Enter your guess value: ")
        if k.isdigit():
            l=int(k)
            break
        else:
            print("Enter a number!!")
    return l

def random(y,z): 
    f=rad.randint(y,z)
    return f


y,z=take_input() #receives value from input taking fuction
rnd=random(y,z) #sends values to random function and gets the number

def chance_count(): #gives a chance couhnt if lucky then max chances if unlucky then min chances
    o=rad.randint(7,15)
    return o

count = chance_count() # receives values
print("total chances",count)
while count > 0: #keeps going till count hit 0
    guess=check_guess()
    if guess == rnd:
        print("YOU GUESSED RIGHT!!!!!")
        break
    else:
        print("not right")
        print("guesses left",count-1)
        count-=1
else: #if count hit zero then this executes
    print("Number was: ",rnd)
