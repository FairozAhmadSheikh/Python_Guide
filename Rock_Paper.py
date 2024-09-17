import sys
import random
print("Welcome To Rock Paper and Scissors :")

player_choice=input("Enter Your choice:  \n 1 for rock \n 2 for paper \n 3 for scissors : ");
player=int(player_choice);

if player<1 or player>3:
    sys.exit("Select correct one among 3 options ")

comuter_choice=random.choice("123")
computer=int(comuter_choice)
print("You choose ",player_choice)
print("Computer Choose ",comuter_choice)

if player==computer:
    print("Round Tie!")
elif player==1 and computer==2:
    print("You win")
elif player==3 and computer==2:
    print("You win")
elif player==2 and computer==1:
    print("You win")
else:
    print("You Loose")