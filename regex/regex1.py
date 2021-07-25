# 정규표현식
# 특정한 패턴과 일치하는 문자열을 검색, 치환, 제거
# 정규표현식의 도움 없이 패턴을 찾을 수 있긴 하지만, 불완전하거나 작업의 cost가 높음
import re

# search() : 패턴 매칭, 매칭된 결과값을 Match 객체로 리턴

# 패턴 설정
# compile() : 표현식에 대해 RegexObject 객체로 저장
pattern = re.compile("D.A")

result = pattern.search("DAA")
print(result)  # <re.Match object; span=(0, 3), match='DAA'>
print(result.start(), result.end(), result.group())  # 0 3 DAA

print("\nraw string 사용")
result = re.search(r"D.A", r"DAA")
print(result)


print("\n원본 문자열에 일치하는 패턴이 없는 경우")
print(pattern.search("D00A"))  # None
print(pattern.search("DA"))
print(pattern.search("d0A"))

print(pattern.search("d0A D1A 0111"))  # <re.Match object; span=(4, 7), match='D1A'>
