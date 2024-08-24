#!/usr/bin/env python3.11
class MyClass:
    def __init__(self):
        self.__private_var = 42  # This will be name-mangled

    def __private_method(self):
        print("This is a private method")

    def access_private(self):
        return self.__private_var

class SubClass(MyClass):
    def __init__(self):
        super().__init__()
        self.__private_var = 99  # This creates a new variable, not overriding MyClass.__private_var

    def try_access_private_method(self):
        self.__private_method()  # This will raise an AttributeError

# Usage
obj = MyClass()
print(obj.access_private())  # Output: 42
#print(obj.__private_var)  # This would raise an AttributeError

sub_obj = SubClass()
print(sub_obj.access_private())  # Output: 42
print(sub_obj._SubClass__private_var)  # Output: 99, since it's a different variable
#print(sub_obj.try_access_private_method()) 

# Accessing the mangled name
print(obj._MyClass__private_var)  # Output: 42
