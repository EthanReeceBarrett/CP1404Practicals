"""subclass of taxi"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Taxi, but FANCY"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """returns string value for SST"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """get current fair"""
        return self.flagfall + super().get_fare()
