import re

s = "hello from python"

i = re.findall("on$", s)

if (i):
    print("String Match")
else:
    print("No match")