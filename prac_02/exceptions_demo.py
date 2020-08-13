"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # while loop avoids the use of the exception
    while denominator < 1:
        denominator = int(input("Enter a non-Zero denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

# except ZeroDivisionError:
#     print("Cannot divide by zero!")

print("Finished.")

# Q1: a ValueError occurs when an entered value is NOT an Integer

# Q2: a ZeroDivisionError will occur when the values entered results in a divide by 0, which is considered a
# mathematical impossibility

# Q3: it could be removed using a while loop based of inputs from the user
