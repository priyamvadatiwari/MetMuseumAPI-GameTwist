import json
import os
import random
import time

path = 'players'
if not os.path.exists(path):
  os.makedirs(path)

def login():
    question = input("Do you have an account? y/n ")
    if question.lower() == 'y':
        print("Please enter your account information")
        username = input("Username: ")
        password = input("Password: ")
        try:
            with open(os.path.join(path, username + ".json"), "r") as game:
                info = json.load(game)

            if info["username"] == username and info["password"] == password:
                print("Welcome to your game account", username.title() + "!")

                #saves current file
                with open("current_player.json", "w") as file:
                    json.dump(info, file)
            else:
                print("Incorrect username or password")
        except FileNotFoundError:
            print("We can not find that account\n Please try again")
            login()
            
            
    elif question.lower() == 'n':
        signup()
    else:
        print("Please make a valid selection")

def signup():
    print("Fill in your information to create an account!")
    username = input("Username: ")
    password = input("Password: ")
    
    info = {}
    info["username"] = username
    info["password"] = password
    info["progress"] = 0
    info["health"] = 0
    info["money"] = 0
    info["items"] = []
    info["account_start"] = time.time()
    
    with open(os.path.join(path, username + ".json"), "w") as infile:
        info = json.dump(info, infile)

    login()

login()