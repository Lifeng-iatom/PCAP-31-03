#!/usr/bin/env python3.11
import sys
from cli import main
from cli.error import ArgumentsError

try:
      main()
except (ArgumentsError,AssertionError) as err:
      print(f"error:{err}")
      sys.exit(1)