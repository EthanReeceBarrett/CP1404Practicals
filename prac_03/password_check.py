"""Password check Program
checks user input length and and print * password if valid, BUT with functions"""

minimum_length = 3

def main():
    password = get_password(minimum_length)
    convert_password(password)


def convert_password(password):
    """converts password input to an equal length "*" output"""
    for char in password:
        print("*", end="")


def get_password(minimum_length):
    """takes a users input and checks that it is greater than the minimum length
    if not, repeats till valid then returns the password"""
    valid = False
    while not valid:
        password = input("Please enter password greater than 3 characters long: ")
        password_count = 0
        for char in password:
            password_count += 1
        if password_count <= minimum_length:
            print("invalid password")
        else:
            print("valid password")
            valid = True
    return password

main()
