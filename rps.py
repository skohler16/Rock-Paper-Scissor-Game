from random import randint

t = ["Rock", "Paper", "Scissor"]

computer = t[randint(0,2)]
Player = False

print(computer)

while Player == False:
    Player = input('Rock, Paper, Scissor?')
    if Player == computer:
        print("tie!!")
    elif Player == "Rock":
        if computer == "Paper":
            print("You loose!!", computer, "covers", Player, "!!")
        else:
            print("Winner!", Player, "crushes ", computer, "!!!")
    elif Player == "Paper":
        if computer == "Scissors":
            print("You loose", computer, "cuts", Player)
        else:
            print("Winner!", Player, "covers", computer)
    elif Player == "Scissor":
        if computer == "Rock":
            print("You loose",  computer, "smashes", Player)
        else:
            print("Winner!", Player, "cuts", computer)
    else:
        print("That is not a valid input, Please check your spelling and try again!")



Player = False
computer = t[randint(0, 2)]

