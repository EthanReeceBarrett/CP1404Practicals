"""Warm up activity for week 4 prac"""

numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0]) # takes the first element:3
print(numbers[-1]) # takes the last element:2
print(numbers[:-1]) # displays all elements: 3 1 4 1 5 9 2 (edit displays all without the last input)
print(numbers[3:4]) # displays elements 3 and 4: 1 5 (displays just element 3: 1)
print(5 in numbers) # logical check to see if 5 is in numbers: True
print(7 in numbers) # logical check to see if 7 is in numbers: False
print("3" in numbers) # logical check to see if string "3" is in numbers: False
print(numbers + [6, 5, 3]) # adds 6, 5 and 3 to the end of numbers

numbers[0] = "10"
numbers[-1] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)
