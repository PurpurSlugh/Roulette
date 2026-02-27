import random
from colorama import Fore, Back, Style, init

init()
money = 1000

while True:
    print(f"\nYou have {money}$")
    

    bet_input = input("How much do you want to bet? ")
    if not bet_input.isdigit():
        print("Please enter a valid number")
        continue
    cashout = int(bet_input)
    
    if cashout > money:
        print("You don't have enough money!")
        continue

    print("Please select a number (It's optional)!")
    print("Select x if don't want to bet on the number!")
    number = input().lower()
    
    print("Please select a color!")
    color = input().lower()
    colors = ""

    gamble = random.randint(0, 36)
    print("\nResult: ", end="")
    if (gamble == 0):
        print(Fore.GREEN, gamble, Style.RESET_ALL)
        colors = "green"
    elif gamble in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
        print(Fore.RED, gamble, Style.RESET_ALL)
        colors = "red"
    else:
        print(Back.WHITE, Fore.BLACK, gamble, Style.RESET_ALL)
        colors = "black"

    
    won = False
    

    if number != "x" and number.isdigit() and int(number) == gamble:
        print("YOU SELECTED THE CORRECT NUMBER!")
        money = money + (cashout * 35)
        won = True
    

    if color == colors:
        print("You selected the correct color!")
        money = money + (cashout * 2)
        won = True

    if not won:
        print("You lost your bet.")
        money = money - cashout

    if money <= 0:
        print("Game Over! You are out of money.")
        break
