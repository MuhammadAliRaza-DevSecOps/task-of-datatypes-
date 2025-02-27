# Quiz Game 
"""
print("Welcome Guys to my Computer Quiz ")
playing=input("Do you want to play?")
if playing.lower()!="yes":
    quit()
print("Okay! Let's play the game ")
score=0
answer=input("what is Cpu Stand for ")
if answer.lower()=="Central processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer=input("what is GUI Stand for ")
if answer.lower()=="graphical user interface":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer=input("what is RAM stand for: ")
if answer.lower()=="random access memory":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer=input("what is ROM Stand for ")
if answer.lower()=="read only memory":
    print("correct")
    score+=1
else:
    print("Incorrect")
print("You got " + str(score) + "questions correct ")
print("You Got "+str((score/4)*100)+"%")
"""
# Number Guess 
"""
import random
top_range=input("Type a number: ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("please type a number larger than 0 next time ")
        quit()
else:
    print("Please type  a number next time ")
    quit()
random_number=random.randint(0,top_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time ")
        continue # continue keyword is used for making a loop. 
    if user_guess==random_number:
        print("You got it! Hurray")
        break
    elif user_guess>random_number:
        print("You are above a number ")
    else:
        print("you are below the number")
print("you got it", guesses , "guesses ")
"""
# Rock Paper Sessor Game 
"""
import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
"""
# choose your own advanture:
"""
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
"""

#=================================================Medium===================================

# Password Manager or cracking 
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
