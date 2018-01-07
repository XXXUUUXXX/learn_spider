import re

pattern = re.compile(r"\d+")

m = pattern.search(r"aaa123bbb456")
rm = pattern.search(r"haha 122121 12123 bbaa")

print(m.group(),rm.group())