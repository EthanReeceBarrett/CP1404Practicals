"""program used to simulate the use of different taxis"""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None


def main():
    """prints menu and allows user to use program till user quits"""
    print("Let's drive!")
    total_bill = 0
    user_choice = input("(q)uit, (c)hoose, (d)rive\n>>> ")
    while user_choice.upper() != "Q":
        if user_choice.upper() == "C":
            print("Taxis available")
            choose_taxis(taxis)
            taxi_choice = int(input("choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif user_choice.upper() == "D":
            distance = float(input("How far are you driving: "))
            cost = drive_taxi(current_taxi, distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost))
            total_bill += cost
        else:
            print("Invalid input")
        print("Bill is currently ${:.2f}".format(total_bill))
        user_choice = input("(q)uit, (c)hoose, (d)rive\n>>>")
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    choose_taxis(taxis)


def choose_taxis(taxis):
    """displays taxis to select"""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def drive_taxi(current_taxi, distance):
    """calcs fair, for bills"""
    current_taxi.drive(distance)
    cost = current_taxi.get_fare()
    return cost


if __name__ == '__main__':
    main()
