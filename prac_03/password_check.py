"""Password check Program
checks user input length and and print * password if valid"""

valid = False
while not valid:
    password = input("Please enter password: ")
    password_count = 0
    for char in password:
        password_count += 1
    if password_count <= 3 or password_count >= 10:
        print("invalid password")
    else:
        print("valid password")
        valid = True
for char in password:
    print("*", end="")