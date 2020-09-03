"""Program used to keep track of the users guitars, no error handling"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    my_guitars = []
    input_name = input("Name: ")
    while input_name != "":
        input_year = int(input("Year: "))
        input_price = float(input("Price: "))
        new_guitar = Guitar(input_name, input_year, input_price)
        my_guitars.append(new_guitar)
        print(new_guitar, "Added")
        input_name = input("Name: ")

    # my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(my_guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year,
                                                                  guitar.cost, vintage_string))


main()
