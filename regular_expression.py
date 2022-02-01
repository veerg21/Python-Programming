import re
strg="This meeting will be conducted on 1st and 21st of every month"
strg1="one two three four 5 6 7 8 9 9811008567"
# result=re.findall(r"\d[\w]*", strg)
result=re.findall(r"\w{10}", strg1)
# print(r"\n") #Small R(r) is the starting of a raw string
for r in result:
    print(r)