#slot machine project

import random

def spin_row():
    symbols = [ '🥕', '🥒', '🍌', '🍆', '🌽' ]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🥕':
            return bet * 2
        if row[0] == '🥒':
            return bet * 3
        if row[0] == '🍌':
            return bet * 4
        if row[0] == '🍆':
            return bet * 5
        if row[0] == '🌽':
            return bet * 6
    return 0   # no match → no payout

def main():
    balance = 100
    print("********************************")
    print("    welcome to python slots     ")
    print(" symbols: 🥕, 🥒, 🍌, 🍆, 🌽 ")
    print("********************************")

    while balance > 0:
        print(f"Current balance is {balance}")
        bet = input("Enter the money you wanna gamble: ")
        
        if not bet.isdigit():
            print("❌ The money you wanna gamble should be only positive numbers.")
            continue

        bet = int(bet)   

        if bet > balance:
            print("❌ You cannot bet more than your current balance.")
            continue
    
        if bet <= 0:
            print("❌ The bet must be greater than 0.")
            continue   
        
        row = spin_row()        
        print("spinning..... \n")
        print_row(row)          

        balance -= bet
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 You won {payout}!")
        else:
            print("😢 Sorry, you lost that round.")

        balance += payout

    print("💀 Game over! You ran out of money.")

if __name__ == '__main__':
    main()


