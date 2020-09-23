"""tester file for SST"""

from prac_08.silver_service_taxi import SilverServiceTaxi

rip_off = SilverServiceTaxi("Silver car", 1000, 2)
rip_off.drive(18)
print(rip_off)
print(rip_off.get_fare())