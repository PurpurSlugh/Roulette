import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

balance = 1000
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
MULTIPLIERS = [2, 5, 10, 20, 50, 100, 200, 500]

def get_styled_num(n):
    if n == 0:
        return f"{Back.WHITE}{Fore.GREEN}  0  {Style.RESET_ALL}"
    num_color = Fore.RED if n in RED_NUMBERS else Fore.BLACK
    return f"{Back.WHITE}{num_color}{n:^5}{Style.RESET_ALL}"

row1 = range(3, 37, 3)
row2 = range(2, 36, 3)
row3 = range(1, 35, 3)
offset = "       "

while balance > 0:
   
    num_cycles = random.randint(1, 20)
    lucky_strikes = {}
    
    for _ in range(num_cycles):
        num = random.randint(0, 36)
        mult = random.choice(MULTIPLIERS)
        lucky_strikes[num] = mult

   
    print("\n" + "="*70)
    print(offset + " ".join(get_styled_num(n) for n in row1))
    print(get_styled_num(0) + "  " + " ".join(get_styled_num(n) for n in row2))
    print(offset + " ".join(get_styled_num(n) for n in row3))
    print("="*70)

    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}⚡ LIGHTNING MULTIPLIERS ⚡")
    display_mults = [f"{Fore.CYAN}[{n}: {m}x]{Style.RESET_ALL}" for n, m in lucky_strikes.items()]
    
    for i in range(0, len(display_mults), 5):
        print(" ".join(display_mults[i:i+5]))
    
    print(f"\nBalance: {Fore.GREEN}{balance}$")
    
   
    bet_input = input("Bet amount: ")
    if not bet_input.isdigit(): continue
    
    bet_amount = int(bet_input)
    if bet_amount > balance:
        print(f"{Fore.RED}Insufficient funds!")
        continue

    selected_number = input("Select a number (0-36) or 'x': ").lower()
    selected_color = input("Select color (red/black/green) or 'x': ").lower()

    
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
        
        multiplier = lucky_strikes.get(result, 35)
        
        if result in lucky_strikes:
            print(f"{Fore.YELLOW}{Style.BRIGHT}BOOM! LIGHTNING WIN! {multiplier}x")
        else:
            print(f"STRAIGHT UP! You hit {result}!")
            
        current_win += (bet_amount * multiplier)
        won_bet = True

    if selected_color == win_color:
        print(f"Color match: {win_color.upper()}!")
        current_win += (bet_amount * 2)
        won_bet = True


    if won_bet:
        balance += current_win
        print(f"{Fore.GREEN}Total win: {current_win}$")
    else:
        balance -= bet_amount
        print(f"{Fore.RED}Loss: -{bet_amount}$")

print(f"\n{Fore.RED}{Style.BRIGHT}Game Over! You're broke.")
