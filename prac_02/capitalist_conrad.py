"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# MAX_INCREASE = 0.1  # 10%
# Change MAX_INCREASE to 17.5%
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05  # 5%
# MIN_PRICE = 0.01
# change MIN_PRICE to $1
MIN_PRICE = 1.0
# MAX_PRICE = 1000.0
# change MAX_PRICE to $100
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
DAY = 0

price = INITIAL_PRICE

# Create a new file named OUTPUT.txt, or edit a file named such
OUTPUT_FILE = "OUTPUT.txt"
out_file = open(OUTPUT_FILE, 'w')

# prints to file
print("on day {}, the price was ${:,.2f}".format(DAY, price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    DAY = DAY + 1
    price *= (1 + price_change)
    
    # Prints to file
    print("on day {}, the price was ${:,.2f}".format(DAY, price), file=out_file)
out_file.close()
