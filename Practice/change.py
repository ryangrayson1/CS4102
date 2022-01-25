# A simple python algorithm to calculate change

import math

price = float(input("Enter Price: $"))
payment = float(input("Enter Payment: $"))

twenties = 0
tens = 0
fives = 0
ones = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

def change1(price, payment):
    amount_left = round((payment - price) * 100)
    if amount_left < 0:
        print("insufficient funds given!")
        return

    while amount_left > 0:

        print(amount_left)
        if amount_left >= 2000:
            global twenties
            twenties += amount_left // 2000
            amount_left -= twenties * 2000
        
        elif amount_left >= 1000:
            global tens
            tens += amount_left // 1000
            amount_left -= tens * 1000
        
        elif amount_left >= 500:
            global fives
            fives += amount_left // 500
            amount_left -= fives * 500

        elif amount_left >= 100:
            global ones
            ones += amount_left // 100
            amount_left -= ones
            
        elif amount_left >= 25:
            global quarters
            quarters += math.floor(amount_left / 25)
            amount_left -= quarters * 25

        elif amount_left >= 10:
            global dimes
            dimes += math.floor(amount_left / 10)
            amount_left -= dimes * 10

        elif amount_left >= 5:
            global nickels
            nickels += math.floor(amount_left / 5)
            amount_left -= nickels * 5

        else:
            global pennies
            print(str(amount_left))
            pennies += math.floor(amount_left / 1)
            amount_left -= pennies * 1

change1(price, payment)

print("Change for a payment of " + str(payment) + " and a price of " + str(price) + " is:")

if (twenties > 0):
    print(" twenties, ", end="")
if (tens > 0):
    print(str(round(tens)) + " tens, ", end='')
if (fives > 0):
    print(str(round(fives)) + " fives, ", end='')
if (ones > 0):
    print(str(round(ones)) + " ones, ", end='')
if (quarters > 0):
    print(str(round(quarters)) + " quarters, ", end='')
if (dimes > 0):
    print(str(round(dimes)) + " dimes, ", end='')
if (nickels > 0):
    print(str(round(nickels)) + " nickels, ", end='')
if (pennies > 0):
    print(str(round(pennies)) + " pennies, ", end='')