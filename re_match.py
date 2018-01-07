import re

# re.I忽略大小写
pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)
m = pattern.match("Hello world hello Python")
print(m.group())
