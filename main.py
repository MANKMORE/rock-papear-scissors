import random
from colorama import Fore, Back, Style

playing = True

while playing:
    player_input = input("pick an answer (1 = rock, 2 = paper, 3 = scissors), type exit to quit: ")
    if player_input == "exit":
        playing = False
        break
    aiasnwer = random.randint(1, 3)

    inputInt = 0

    if player_input == "1":
        inputInt = 1
    elif player_input == "2":
        inputInt = 2
    elif player_input == "3":
        inputInt = 3


    # assign data
    cars = ["rock", "paper", "scissors"]

    if aiasnwer + 1 == 4:
        if player_input == "1":
            print(Fore.GREEN +  "rock " + Fore.GREEN + "beats scissors"  + Style.RESET_ALL)
    elif aiasnwer - 1 == 0 and player_input == "3":
        print(Fore.RED + "rock " + Fore.RED + "beats scissors"  + Style.RESET_ALL)
    elif aiasnwer + 1 == inputInt:
        print(Fore.GREEN + cars[inputInt - 1] + " beats " + cars[aiasnwer - 1]  + Style.RESET_ALL)
    elif aiasnwer - 1 == inputInt:
        print(Fore.RED + cars[aiasnwer - 1] + " beats " + cars[inputInt - 1]  + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "tie"  + Style.RESET_ALL)

    print("ai answer: " + cars[aiasnwer - 1])
    print("you picked: " + cars[inputInt - 1])
