#!/usr/bin/env python3.11

from car import Car
from boat import Boat

class AmphibiousVehicle(Car, Boat):
      def __init__(self,engine,tires=[],distance_traveled=0,unit='miles'):
            super().__init__(engine=engine,tires=tires,distance_traveled=distance_traveled,unit=unit)
            self.boat_type = 'motor'

      def travel(self,land_distance=0,water_distance=0):
            self.voyage(water_distance)
            self.drive(land_distance)


water_car = AmphibiousVehicle('4-C')
water_car.travel(10,20)
print(water_car.description())

