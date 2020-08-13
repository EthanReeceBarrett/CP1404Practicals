import random

print(random.randint(5, 20))
"""the first line prints a random number between 5 and 20"""
print(random.randrange(3, 10, 2))
"""The second line prints a random number between 3 and 10 in steps of 2. 
As a result of the odd stepping, the highest value can only be 9
this line could not produce a 4"""
print(random.uniform(2.5, 5.5))
"""It is assumed that the smallest number i could see is 2.5 and the largest is to be 5.5
however do to the extreme amounts of decimals it is very unlikely"""

# tasked code

print(random.randint(1, 100))

# wanted to test that the values generated were inclusive

# random_test = random.randint(1, 100)
# while random_test < 100:
#     random_test = random.randint(1,100)
# print(random_test)
