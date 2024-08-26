import sys

from .error import ArgumentsError

def main():
      #if len(sys.argv) < 2:
      #raise ArgumentsError('not enough args')
      assert len(sys.argv)>=2,"too few args"
      print(f"name is {sys.argv[1]}")