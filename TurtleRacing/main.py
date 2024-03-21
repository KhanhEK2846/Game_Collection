import turtle,time,random

WIDTH,HEIGHT =500,500
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_races() -> int:
    racers = 0
    while True:
        racers = input("Number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range")

def get_predict_win_turtle(colors:"list")-> int:
    guess = 0
    for i,color in enumerate(colors):
        print(f'No. {i+1} - Turtle {color}')
    while True:
        guess = input("Enter Winner Turtle No.: ")
        if guess.isdigit():
            guess = int(guess)
        else: 
            print("Invalid input")
            continue
        
        if 1 <= guess <= len(colors):
            return guess -1
        else:
            print(f"There is no Turtle No.{guess}")


def race(colors:"list")-> str:
    init_turtle()
    turtles = create_turtle(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y >= HEIGHT //2 -10:
                return colors[turtles.index(racer)]
            

def create_turtle(colors:"list") -> list:
    turtles = []
    spacingx = WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) # Since default was right
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles
    
    

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing')


if __name__ == "__main__":
    racers = get_number_of_races()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    predict = get_predict_win_turtle(colors)
    winner = race(colors)
    print(f'Winner Turtle is No.{colors.index(winner)} - {winner}')
    
    if predict == colors.index(winner):
        print("You win")
    else:
        print("Better luck next time")
    
    time.sleep(10)
    
    
    
    
