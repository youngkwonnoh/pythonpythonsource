import re
from typing import Pattern

print("[] : 괄호안에 들어가는 문자가 들어있는 패턴")
pattern = re.compile("[abcdefgABCDEFG]")
print(pattern.search("a1234"))
print(pattern.search("abc1234"))
print(pattern.search("abcz1234"))
print(pattern.search("CbAB1234"))
print("\n")
print("[-] : 괄호안에 들어가는 문자를 범위로 나타내기")
pattern = re.compile("[a-gA-G]")
print(pattern.search("a1234"))
print(pattern.search("abc1234"))
print(pattern.search("abcz1234"))
print(pattern.search("CbAB1234"))
print("\n")
pattern = re.compile("[a-zA-Z]")
print(pattern.search("Z1234"))
print("\n")
pattern = re.compile("[a-zA-Z0-9]")
print(pattern.search("Z1234"))

print("[] 안에서 [ 바로 뒤에 ^ 사용하기 : 뒤에 오는 문자가 아닌 패턴 찾기")
pattern = re.compile("[^a-zA-Z0-9]")
print(pattern.search("Z1234"))  # None
print(pattern.search("가나다라"))  # <re.Match object; span=(0, 1), match='가'>
print(pattern.search("!@$#@$3"))  # <re.Match object; span=(0, 1), match='!'>
print("\n")
print("한글 찾기")
pattern = re.compile("[가-힣]")  # [ㄱ - ㅎ ㅏ - ㅣ 가-힣]
print(pattern.search("abc가나다라"))  # <re.Match object; span=(3, 4), match='가'>
print(pattern.search("나다라"))  # <re.Match object; span=(0, 1), match='나'>
