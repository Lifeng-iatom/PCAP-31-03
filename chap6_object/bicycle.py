#!/usr/bin/env python3.11
from vehicle import Vehicle

class Bicycle(Vehicle):

      def __init__(self,tires=None,distance_traveled=0,unit='miles'):
            super().__init__(distance_traveled,unit)

            if not tires:
                  tires=[self.de_tires,self.de_tires]
            self.tires = tires
      
      def description(self):
            initial = super().description()
            return f"{initial} on {len(self.tires)} tires"

bike =Bicycle(["1","2"],100,"km")
print(bike.description())

honda = Vehicle(2000)
print(honda.description())
