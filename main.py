import os
import sys
import json
import time
import platform

version = "0.1.0"

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def setup():
    ln_write(r"""
 ________   ________  ___  ___  ________  ___    ___ 
|\   ____\ |\   ____\|\  \|\  \|\   __  \|\  \  /  /|
\ \  \___|_\ \  \___|\ \  \\\  \ \  \|\  \ \  \/  / /
 \ \_____  \\ \_____  \ \   __  \ \   ____\ \    / / 
  \|____|\  \\|____|\  \ \  \ \  \ \  \___|\/  /  /  
    ____\_\  \ ____\_\  \ \__\ \__\ \__\ __/  / /    
   |\_________\\_________\|__|\|__|\|__||\___/ /     
   \|_________\|_________|              \|___|/                                  
        """)
    print("Welcome to ssh py setup.")
    print("We need to configure some ssh hosts to connect to later.")
    print("We will ask you for the hostname and the username you will have to enter the password manually whe you connect to your host.")
    print("For example:")
    print("\tadmin@server")
    print("\troot@70.2.64.12")
    hosts = []
    config = {}
    while True:
        hosts.append(input("Host: "))
        if input("Add another host? (y/n): ").upper() == "N":
            break
    print("If you ever want to add or delete a host you can go to "+os.getcwd()+"/config.json and edit the hosts list")
    config["hosts"] = hosts
    config["newuser"] = False
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)

def ln_write(str):
    for line in str.split("\n"):
        print(line)
        time.sleep(0.02)
    print("\n")


def char_write(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()        
        time.sleep(0.01)
    print("\n")

def main():
    ln_write(r"""
 ________   ________  ___  ___  ________  ___    ___ 
|\   ____\ |\   ____\|\  \|\  \|\   __  \|\  \  /  /|
\ \  \___|_\ \  \___|\ \  \\\  \ \  \|\  \ \  \/  / /
 \ \_____  \\ \_____  \ \   __  \ \   ____\ \    / / 
  \|____|\  \\|____|\  \ \  \ \  \ \  \___|\/  /  /  
    ____\_\  \ ____\_\  \ \__\ \__\ \__\ __/  / /    
   |\_________\\_________\|__|\|__|\|__||\___/ /     
   \|_________\|_________|              \|___|/                                  
        """)
    char_write("A simple SSH manager for the windows terminal")
    print("Version:"+str(version)+ " running on "+platform.system()+" "+platform.release())
    print("#| Host")
    with open('config.json') as json_file:
        config = json.load(json_file)
    for i in config["hosts"]:
        print(str(config["hosts"].index(i)+1)+"| "+i)
    try:

        ask = input("\nChoose a host number: ")
    except KeyboardInterrupt:
        sys.exit(0)
    if ask == "exit" or ask == "quit":
        sys.exit(0)
    clear_screen()
    os.system("ssh "+config["hosts"][int(ask)-1])

if __name__ == "__main__":
    with open('config.json') as json_file:
        config = json.load(json_file)
    if config["newuser"] == True:
        setup()
    clear_screen()
    main()