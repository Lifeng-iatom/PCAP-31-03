#!/usr/bin/env python3.11
import sys

if len(sys.argv) < 2:
      raise Exception('not enough args')

name = sys.argv[1]
print(f"name is {name}")