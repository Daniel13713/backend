#!/usr/bin/python3
"""
This module explain regex funtionalities
"""

# First, Other options before use re module
s = "foo123bar"
p = "123"

# write Python code to find out whether s contains the substring '123'
print(p in s)

# If you want to know not only whether '123' exists in s but also where it exists
print(s.find(p))
print(s.index(p))

import re

# re.rearch()
"""
The return value is always the leftmost possible match. re.search() scans the search string from left to right, and as soon as it locates a match for <regex>, it stops scanning and returns the match.
"""

with open("text.txt", mode="r", encoding="utf-8") as file:
    readed = file.read()
    # print(re.search("[0-9][0-9] [g-z]", readed) #hezadecimal digit characters [0-9a-fA-f]
    print(re.search(r"\\", readed))
