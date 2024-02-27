import random
import math

low = int(input("Lower Number Bound:  "))
high = int(input("Upper Number Bound:  "))

def Guest(lower,upper):
    x = random.randint(lower, upper)
    chance = round(math.log(upper - lower + 1, 2))
    print("You have " + str(chance) + " to play \n")
    while True:
        guess = int(input(" Your guess number: "))
        chance = chance - 1
        if x == guess:
            print("You did it")
            return
        elif chance > 0:
            if x < guess:
                print("Too High")
            else:
                print("Too Small")
            print("You have "+ str(chance) + " left")
        else: 
            print("You're a loser !!!\n The number is: " + str(x))
            return
        
if low < high:
    Guest(low,high)
else:
    print("Sorry for thinking you know the difference between large and small numbers")
