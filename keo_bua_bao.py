from random import randint

player = input()
computer = randint(0,2)

if computer == 0:
    computer = "keo"
if computer == 1:
    computer = "bua"
if computer == 2:
    computer = "bao"
    
print("you choose:" + player)
print("computer choose: " + computer)

if player == computer:
    print("draw")
else:
    if player == "keo":
        if computer == "bua":
            print("lose")
        else:
            print("win")
    if player == "bua":
        if computer == "keo":
            print("win")
        else:
            print("lose")
    if player == "bao":
        if computer == "keo":
            print("lose")
        else:
            print("win")