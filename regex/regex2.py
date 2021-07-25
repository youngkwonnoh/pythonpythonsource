import re
from typing import Pattern

print("***** 반 복 *****")
print("? : 최소 0 ~ 최대 1")
pattern = re.compile("D?A")  # D가 없어도 되고, 있다면 D는 하나만 나오면 됨
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("AA"))
print("\n")
print("* : 최소  ~ 최대 무한대")
pattern = re.compile("D*A")  # D가 없어도 되고, 있다면 D는 최대한 많이 나오면 됨
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("AA"))
print(pattern.search("DDDDDDDDDDDDA"))
print("\n")
print("+ : 최소 1  ~ 최대 무한대")
pattern = re.compile("D+A")  # D가 무조건 하나는 있어야 되고, 있다면 D는 최대한 많이 나오면 됨
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("AA"))
print(pattern.search("DDDDDDDDDDDDA"))
print("\n")
print("{n} 사용법")
pattern = re.compile("AD{2}A")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))
print(pattern.search("ADDDA"))  # None
print("\n")
print("{n,m} 사용법")
pattern = re.compile("AD{2,6}A")
print(pattern.search("ADDA"))  # None
print(pattern.search("ADDDA"))
print(pattern.search("ADDDDDDA"))  # None
