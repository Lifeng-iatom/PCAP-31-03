#!/usr/bin/env python3.11
import math
from strhelper import reverse
from str_shuffle import shuffle

name = "Kevin Bacon"

assert math.ceil(14.11) == 15, f"Expected 15, but got {math.ceil(14.11)}"
assert (
    reverse(name) == "nocaB niveK"
), f"Expected 'nocaB niveK', but got {reverse(name)}"
assert type(shuffle(name)) == str, f"Expected a string, but got {type(shuffle(name))}"
assert sorted(shuffle(name)) == sorted(
    name
), f"Expected [' ', 'B', 'K', 'a', 'c', 'e', 'i', 'n', 'n', 'o', 'v'], but got {sorted(shuffle(name))}"