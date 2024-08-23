#!/usr/bin/env python3.11
people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 66},
    {"name": "Victor Wong", "age": 74},
]

sorted_by_name = sorted(people,key=lambda s: s["name"].lower())
print(sorted_by_name)

name_declarations = map(lambda d:f"{d['name']} is {d['age']} years old",sorted_by_name)
print(list(name_declarations))

under_seventy = filter(lambda d: d['age']<70,sorted_by_name)
under_seventy = sorted(under_seventy,key=lambda d: d['age'])
print(list(under_seventy))
