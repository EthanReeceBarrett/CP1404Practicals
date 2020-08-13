""" Question 1
Write code that asks the user for their name,
then opens a file called "name.txt" and writes that name to it."""

name_txt = "name.txt"
output_file_1 = open(name_txt, "w")

# reads users name, saves it to name.txt
user_name = input("what is your name? ")
user_name = user_name.title()
print("{}".format(user_name), file=output_file_1)

output_file_1.close()

"""Question 2
Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file)."""

input_file_1 = open(name_txt, "r")

# prints users name from name.txt
user_name = input_file_1.readline()
print("Your name is {}".format(user_name))

input_file_1.close()

"""Question 3
Create a text file called numbers.txt and save it in your prac_02 directory. 
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", 
reads only the first two numbers and adds them together then prints the result, 
which should be... 59.
"""
numbers_txt = "numbers.txt"
input_file_2 = open(numbers_txt, 'r')

# reads first 2 numbers and adds them
number_1 = int(input_file_2.readline())
number_2 = int(input_file_2.readline())
number_total = number_1 + number_2
print(number_total)

"""Question 4
Now write a fourth block of code that prints the total
 for all lines in numbers.txt or a file with any number of numbers."""

input_file_3 = open(numbers_txt, "r")
total = 0
number = 0

# for every line in the document, add each line to a result variable
for line in input_file_3:
    number = int(line)
    total = total + number
print("the Total is: {}".format(total))
input_file_3.close()
