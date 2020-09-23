"""unreliable_car subclass of car"""

from prac_08.car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car that includes Unreliability"""

    def __init__(self, name, fuel, unreliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.unreliability = unreliability

    def drive(self, distance):
        drive_distance = 0
        drive_fail = random.randint(0, 100)
        if drive_fail >= self.unreliability:
            print("{} has failed to drive".format(self.name))
            drive_distance += 0
        else:
            drive_distance = super().drive(distance)
        return drive_distance
