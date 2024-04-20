import pyinputplus as pyip
import random

username=input("Enter Your Username: ")
username = username.capitalize()
choices = ("Rock","Paper", "Scissors" )
def rps(username):

    while True:
        uc=pyip.inputChoice(choices)
        
        cc= random.choice(choices)
        if uc == "Rock" and cc == "Paper":
            print(f"You Lose {username} The Computer Chose{cc}")
            break
        if cc == "Rock" and uc == "Paper":
            print(f"You Win {username} The Computer Chose {cc}")
            break
        if cc == "Scissors" and uc == "Paper":
            print(f"You Lose {username} The Computer Chose {cc}")
            break
            return
        if cc == "Paper" and uc == "Scissors":
            print(f"You Win {username} The Computer Chose {cc}")
            break
        if uc == "Rock" and cc == "Scissors":
            print(f"You Win {username} The Computer Chose {cc}")
            break
        if uc == "Scissors" and cc == "Rock":
            print(f"You Lose {username} The Computer Chose {cc}")
            break
        if uc == cc:
            print("Its a Tie") 
            break
while True:

    rps(username)
    c=input("Would You Like to Play again: Enter Yes or No: ")
    if c == "Yes":
        rps(username)
    else:
        print(f"Thanks For Playing {username}!")
        break