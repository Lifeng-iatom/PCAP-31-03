#!/usr/bin/env python3.11
name =input("put your name here:")

print("your name is long") if len(name)>=6 else print("your name is short")

print("commen letter") if name[0].lower() in ["a","k","j","m"] else print("not common letter")

for letter in name:
      print(f"{letter} this is a vowel") if letter.lower() in ["a","e","i","o","u"] else print(f"{letter} not a vowel")