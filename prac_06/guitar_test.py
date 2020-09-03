""" code used to test guitar class, i dont know guitars all that well"""


from prac_06.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)
    print("{} get_age() - Expected 98. got {}".format(guitar1.name, guitar1.get_age()))
    print("{} get_age() - Expected 7. got {}".format(guitar2.name, guitar2.get_age()))
    print("{} is_vintage() - Expected True. got {}".format(guitar1.name, guitar1.is_vintage()))
    print("{} is_vintage() - Expected False. got {}".format(guitar2.name, guitar2.is_vintage()))


main()
