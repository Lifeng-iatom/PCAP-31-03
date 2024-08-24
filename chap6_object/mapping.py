#!/usr/bin/env python3.11
class Mapping:
      def __init__(self,iterable):
            self.itemlist = []
            self.__update(iterable)
      
      def update(self,iterable):
            for item in iterable:
                  self.itemlist.append(item)

      __update = update

class Mappingsubclass(Mapping):
      def update(self,keys,values):
            for item in zip(keys,values):
                  self.itemlist.append(item)

      def printsome(self):
            print("something")

      __update = printsome

print(dir(Mapping))
print(dir(Mappingsubclass))