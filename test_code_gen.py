#!/usr/bin/python3

from game_logic.code_gen import generate_code_no_dups
from game_logic.code_gen import generate_code_dups

print("TEST: no duplicate code - 4, 8 digits long")
print(generate_code_no_dups(4))
print(generate_code_no_dups(8))

print("-")

print("TEST: Duplicates possible - 4, 8 digits long")
print(generate_code_dups(4))
print(generate_code_dups(8))
print(generate_code_dups(16))
