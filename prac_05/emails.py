"""emails
a program that excepts a users email, and creates an assumed name from the email and adds it to a list
"""


def main():
    emails_and_names = {}
    email = input("What is your Email? ")
    while email != "":
        name = email_to_name(email)
        confirm_name = input("Is your name {}? (y/n) ".format(name)).upper()
        invalid = False
        while not invalid:
            if confirm_name == "Y" or confirm_name == "":
                emails_and_names[email] = name
                invalid = True
            elif confirm_name == "N":
                name = input("please state your name: ")
                emails_and_names[email] = name
                invalid = True
            else:
                print("INVALID INPUT")
        email = input("What is your Email? ")
    for email, name in emails_and_names.items():
        print("{} ({})".format(name, email))


def email_to_name(emails):
    """takes the prefix of the email as the name"""
    prefix = emails.split("@")[0]
    name = prefix.split(".")
    name = " ".join(name).title()
    return name


main()
