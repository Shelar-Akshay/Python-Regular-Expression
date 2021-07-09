import re

s = "Hello from Python, This is Reg Expression"

i = re.search("^Hello", s)
# ^Starts with

if (i):
    print("String Match!")
else:
    print("No match")