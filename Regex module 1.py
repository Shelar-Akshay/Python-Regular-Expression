import re

s = "Hello from Python, This is Reg Expression"

i = re.search("^Hello", s)
# ^Starts with

if (i):
    print("Python Developer")
else:
    print("No match")