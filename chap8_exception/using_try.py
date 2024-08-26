#!/usr/bin/env python3.11
import sys
import random
try:
      print(f"first argument {sys.argv[1]}")
      args = sys.argv
      random.shuffle(args)
      print(f"random args {args[0]}")
except (IndexError,KeyError) as err:
      print(f"Error:no argument,pls provide one({err})")
      sys.exit(1)
except NameError:
      print(f"Error:random not import")
      sys.exit(1)
else:
      print("else is running")
finally:
      print("finally is running")