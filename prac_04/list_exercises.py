"""prac 4 list fun and Woefully inadequate security checker"""


def main():
    numbers = get_numbers()
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    # print(numbers)
    print("the first number is {}".format(numbers[0]))
    print("the last number is {}".format(numbers[-1]))
    print("the smallest number is {}".format(min(numbers)))
    print("the largest number is {}".format(max(numbers)))
    average_num = average(numbers)
    print("the average of the numbers is {}".format(average_num))
    username_test(usernames)


def get_numbers():
    """grabs a total number of numbers (base functionality is 5) and asks for a number value for each number
    to be stored in a list"""
    # amount_of_numbers = int(input("How many Numbers? "))
    amount_of_numbers = 5
    numbers = []
    for number in range(1, amount_of_numbers+1):
        numbers.append(int(input("what is number {}? ".format(number))))
    return numbers


def average(numbers):
    average_num = sum(numbers)/len(numbers)
    return average_num


def username_test(usernames):
    enter_username = input("Please enter your username: ")
    if enter_username in usernames:
        print("access granted")
    else:
        print("access denied")


main()
