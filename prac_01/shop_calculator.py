
number_of_items = int(input("Number of items: "))
price_of_item_total = 0

# repeats question till valid input
while number_of_items < 1:
    print("Invalid response, please try again")
    number_of_items = int(input("Number of items: "))

# creates a total price from input prices, repeats for desired number of items
for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    price_of_item_total = price_of_item_total + price_of_item
print("The Total price of", number_of_items, "items is: $", price_of_item_total)