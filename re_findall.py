import re

m = re.findall(r"\d+", "hello 21 345 6788")
#print(m)

pattern = re.compile(r"\d+")
m2 = pattern.findall("haha 231 51 123456")
print(m2)

pattern = re.compile(r"\d?")
m3 = pattern.findall("haha 231 51 123456")
print(m3)

pattern = re.compile(r"\d*")
m4 = pattern.findall("haha 231 51 123456")
print(m4)

