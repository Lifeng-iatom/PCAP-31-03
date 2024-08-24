#!/usr/bin/env python3.11
from random import shuffle as a_shffle
def shuffle(name):
      namelist = list(name)
      a_shffle(namelist)
      return "".join(namelist)