import random as rad;

def check_upper():
    while True:
        m = input("Enter a upper value: ")
        if m.isdigit():
            n=int(m)
            break
        else:
            print("Enter a number!!")
    return n

def check_lower():
    while True:
        c = input("Enter your lower value: ")
        if c.isdigit():
            d=int(c)
            break
        else:
            print("Enter a number!!")
    return d

def take_input():
    a=check_lower()
    b=check_upper()
    return a,b

def check_guess():
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


y,z=take_input()
rnd=random(y,z)

def chance_count():
    o=rad.randint(7,15)
    return o

count = chance_count()
print("total chances",count)
while count > 0:
    guess=check_guess()
    if guess == rnd:
        print("YOU GUESSED RIGHT!!!!!")
        break
    else:
        print("not right")
        print("guesses left",count-1)
        count-=1
else:
    print("Number was: ",rnd)