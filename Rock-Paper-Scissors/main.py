#Rock Paper Scissors
import random

Choice = {1:"Rock",2:"Paper",3:"Scissors"}
Result = {1:"You Lose",2:"Draw",3:"You Win"}

while True:
    print("1 - Rock \t 2 - Paper \t 3 - Scissors \n")
    Player = int(input("Your choice: "))
    if Player > 3 or Player < 0 :
        print("Illegal \n")
        continue
    Computer = random.randint(1,3)
    print("Player: " + Choice[Player] + " - Computer: " + Choice[Computer] + '\n')
    if Player == Computer:
        print(Result[2])
    elif Player == 1:
        if Computer == 2:
            print(Result[1])
        else:
            print(Result[3])
    elif Player == 2:
        if Computer == 1:
            print(Result[3])
        else:
            print(Result[1])
    elif Player == 3:
        if Computer == 1:
            print(Result[1])
        else:
            print(Result[3])
    
    