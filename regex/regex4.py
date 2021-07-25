import re

# sub(패턴, 바꿀문자열, 원본문자열) : 찾아서 바꾸기
# search() : 문자열 전체를 검색해서 매칭되는 패턴을 찾아서 리턴
# match() : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 리턴

pattern = re.compile("[a-z]+")  # 소문자가 여러개 나올 수 있음
print(pattern.match("True"))  # None
print(pattern.search("True"))  # <re.Match object; span=(1, 4), match='rue'>

print("\n")
print(re.sub("D.A", "Dave", "DDA D1A DDA DA"))

# findall() : 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴
# split() : 찾은 정규식 패턴 문자열을 기준으로 분리
pattern = re.compile("[a-z]+")
print(pattern.findall("Game of Life in Python"))  # ['ame', 'of', 'ife', 'in', 'ython']
pattern = re.compile("[A-Za-z]+")
print(
    pattern.findall("Game of Life in Python")
)  # ['Game', 'of', 'Life', 'in', 'Python']
pattern = re.compile("[a-z]+")
findalled = pattern.findall("GAME")

if len(findalled) > 0:  # if findalled:
    print("정규표현식과 일치하는 문자열이 존재함")
else:
    print("정규표현식과 일치하는 문자열이 존재하지 않음")

print("\n")
pattern = re.compile(":")
print(pattern.split("python:java:script"))  # ['python', 'java', 'script']
