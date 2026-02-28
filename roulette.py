import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

balance = 1000
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

def get_styled_num(n):
    if n == 0:
        return f"{Back.WHITE}{Fore.GREEN}  0  {Style.RESET_ALL}"
    num_color = Fore.RED if n in RED_NUMBERS else Fore.BLACK
    return f"{Back.WHITE}{num_color}{n:^4}{Style.RESET_ALL}"


row1 = range(3, 37, 3)
row2 = range(2, 36, 3)
row3 = range(1, 35, 3)
offset = "      "

while balance > 0:
   
    print("\n" + offset + " ".join(get_styled_num(n) for n in row1))
    print(get_styled_num(0) + " " + " ".join(get_styled_num(n) for n in row2))
    print(offset + " ".join(get_styled_num(n) for n in row3))
    
    print(f"\nBalance: {balance}$")
    bet_input = input("Bet amount: ")
    if not bet_input.isdigit(): continue
    
    bet_amount = int(bet_input)
    if bet_amount > balance:
        print("Insufficient funds!")
        continue

    selected_number = input("Select a number (0-36) or 'x': ").lower()
    selected_color = input("Select color (red/black/green): ").lower()

   
    result = random.randint(0, 36)
    if result == 0:
        win_color = "green"
        display_color = Fore.GREEN
    elif result in RED_NUMBERS:
        win_color = "red"
        display_color = Fore.RED
    else:
        win_color = "black"
        display_color = Fore.BLACK

    print(f"\nResult: {Back.WHITE}{display_color}  {result}  {Style.RESET_ALL}")

 
    won_bet = False
    current_win = 0

  
    if selected_number.isdigit() and int(selected_number) == result:
        print(f"STRAIGHT UP! You hit {result}!")
        current_win += (bet_amount * 35)
        won_bet = True

    
    if selected_color == win_color:
        print(f"Color match: {win_color.upper()}!")
        current_win += (bet_amount * 2)
        won_bet = True

    if won_bet:
        balance += current_win
        print(f"Total win: {current_win}$")
    else:
        balance -= bet_amount
        print(f"Loss: -{bet_amount}$")

print("Game Over!")
