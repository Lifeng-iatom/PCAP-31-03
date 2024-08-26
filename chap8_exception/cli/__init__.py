import sys

from .error import ArgumentsError

def main():
      if len(sys.argv) < 2:
            raise ArgumentsError('not enough args')
      print(f"name is {sys.argv[1]}")