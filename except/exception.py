# 에러
# 컴파일 에러 => 문법적인 에러
print('Test')

a = 10
b = 15
c = 0
print(c) # NameError: name 'c' is not defined

# 런타임 에러
# print(10/0) # ZeroDivisionError : division by zero

x = [10, 20, 30]

print(x[0])
# print(x[3]) # IndexError : list index out of range

dict1 = {"name":"Kim", "age":33, "city":"seoul"}

print(dict1["name"])
# print(dict1["hobby"]) # KeyError : 'hobby'
print(dict1.get("hobby")) # None