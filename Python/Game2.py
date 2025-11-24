import os
from random import randint,uniform
lives=3
contadorTiros=0
def roll_dice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1,dice2
#print(roll_dice)
while True:
    key=input("press any key to roll dices")
    dices=roll_dice()
    print(f"dice1:{dices[0]}")
    print(f"dice2:{dices[1]}")
    if (dices[0]+dices[1])%2==0:
        lives+=1
    else:
        lives-=1
    contadorTiros+=1
    print("lives:",lives)
    print("contador de tiros:",contadorTiros)
    if dices[0]==6 and dices[1]==6:
        print("you win")
        print
        break
    if lives==0:
        print("Game Over")
        print(lives)
        os.system("pause")
        break