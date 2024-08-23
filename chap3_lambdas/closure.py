#!/usr/bin/env python3.11
def greeter(prefix):
      othername = prefix +"lalal"
      def greet(name):
            print(f"{prefix} {name},{othername}")
      return greet

hello = greeter("hello,")
goodbye = greeter("goodbye,")

hello("kevin")
goodbye("kyle")