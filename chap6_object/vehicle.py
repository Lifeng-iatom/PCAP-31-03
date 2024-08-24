#!/usr/bin/env python3.11
class Vehicle:
      """
      vehicle object
      """
      de_tires = 'tire'
      def __init__(self,distance_traveled=0,unit='miles',**kwargs):
            self.distance_traveled = distance_traveled
            self.unit = unit 

     
      def description(self):
            return f"A {self.__class__.__name__} with an {self.distance_traveled} {self.unit}"








