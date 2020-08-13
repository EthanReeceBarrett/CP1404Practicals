"""
CP1404/CP5632 - Practical
Broken program to determine score status, now with functions.
"""
import random

# fixed
def main():
    """runs user score and user random score functions and prints the results"""
    score = user_score()
    print("score is {}".format(score))
    user_random_score = random_score()
    print("random score is {}".format(user_random_score))

def user_score():
    """takes score input and returns result"""
    score = float(input("Enter score: "))
    if score < 0:
        result = "Invalid"
    elif score > 100:
        result = "Invalid"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

def random_score():
    """generates random input and returns result"""
    random_score = random.randint(0,100)
    if random_score < 0:
        result = "Invalid"
    elif random_score > 100:
        result = "Invalid"
    elif random_score > 90:
        result = "Excellent"
    elif random_score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()
