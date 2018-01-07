import re

pattern = re.compile(r"(\w+) (\w+)")

str = "hello 123, hello 456"
m = pattern.sub("hello world",str)

print(m)

m2 = pattern.sub(r"\1 \2", str)
print(m2)