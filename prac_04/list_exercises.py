"""prac 4 list fun and Woefully inadequate security checker"""


def main():
    numbers = get_numbers()
    print(numbers)


def get_numbers():
    """grabs a total number of numbers (base functionality is 5) and asks for a number value for each number
    to be stored in a list"""
    # amount_of_numbers = int(input("How many Numbers? "))
    amount_of_numbers = 5
    numbers = []
    for number in range(1, amount_of_numbers+1):
        numbers.append(input("what is number {}? ".format(number)))
    return numbers


main()
