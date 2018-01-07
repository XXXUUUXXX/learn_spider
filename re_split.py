# coding=utf-8
import re

# 加上r
pattern = re.compile(r"[\s\d\\;]+")

# 加上r，不加r\不会转义
m = pattern.split(r"a bb\aa;mm;  a")
print(m)

m2 = pattern.split(r"a bb\aa;m1m;  123 a")
print(m2)
