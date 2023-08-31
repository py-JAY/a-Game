import random as rad; #the random module because obvious reasons lol

def check_upper(): #checks for value validity
    while True:
        m = input("Enter a upper value: ")
        if m.isdigit():
            n=int(m)
            break
        else:
            print("Enter a number!!");print('\n')
    return n

def check_lower(): # does the same but or lower
    while True:
        c = input("Enter your lower value: ")
        if c.isdigit():
            d=int(c)
            break
        else:
            print("Enter a number!!");print('\n')
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
            print("Enter a number!!");print('\n')
    return l

def random(y,z): 
    f=rad.randint(y,z)
    return f

def chance_count(): #gives a chance count if lucky then max chances if unlucky then min chances
    o=rad.randint(5,15)
    if (o==5):
        print("UNLUCKY LOL")
    elif (o==15):
        print("LUCKY ONE")
    return o


def game():
    y,z=take_input() #receives value from input taking function
    rnd=random(y,z) #sends values to random function and gets the number
    
    count = chance_count() # receives values
    print(f"total chances {count}")
    while count > 0: #keeps going till count hit 0
        guess=check_guess()
        if guess == rnd:
            print("YOU GUESSED RIGHT!!!!!");print('\n')
            break
        else:
            print("not right")
            print(f"guesses left: {count-1}");print('\n')
            count-=1
    else: #when count hits zero this executes
        print(f"Number was: {rnd}");print('\n')
    return
        
def main():
    ans='y'
    while (ans=='y'):
        O=game()
        P=input("Do you want to play more or quit?(q to quit): ");print('\n')
        if P.lower()=='q':
            break
        
        

if __name__=='__main__':
    main()
