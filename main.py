import login 
import json
import random
from stranger import get_advice
from os import system, name

# define our clear function
def clear():
    if name == 'nt': #windows
        _ = system('cls')
    else:
        _ = system('clear') #mac or linux


# read file
with open('game.json', 'r') as myfile:
    data=myfile.read()
# parse file
data = json.loads(data)

room = 0

while True:
    clear()

    chance = random.randint(1,2)
    if chance == 1:
        if data[room]["luck"] == 1:
            print("You are very lucky!")
            #something happens?
    if chance == 2:
        if data[room]["stranger"] == 1:
            print("A stranger walks by and starts talking to you")
            get_advice()
    
    #print(data[room])
    
    print(data[room]["story"])
    
    if data[room]["win"] == 1:
        print("You win the game!")
        #reset 
        break
    
    if data[room]["die"] == 1:
        print("You lose the game!")
        #reset 
        break
    
    print(data[room]["nav"])
    
    choice = input("Please make a selection ")
    try:
        if choice == '1':
            room = data[room]["c1"] - 1
        elif choice == '2':
            room = data[room]["c2"] - 1
        elif choice == '3':
            room = data[room]["c3"] - 1
        else:
            print("Please select a valid option")
    except:
        continue
