# 에러 처리
# try ~ except : 기본
# try ~ except ~ else
# try ~ except ~ else ~ finally
# try ~ finally

print("에러 발생 처리")

x = [10, 20, 30]

try:
    print(x[3])
except:
    print("not found")


#%%
print("안녕하세요")

# %%
name = ["Kim", "Park", "Lee"]

try:
    z = "Let"
    x = name.index(z)  # ValueError
    print("{} found it! in name {1}".format(z, x + 1))
except ValueError:
    print("Not Found")

# %%
dict1 = {"name": "Kim", "age": 33, "city": "seoul"}

try:
    print(dict1["hobby"])
except KeyError:
    print("찾으려는 키가 없음")

# %%
name = ["Kim", "Park", "Lee"]

try:
    z = "Kim"
    x = name.index(z)  # ValueError
    print("{0} found it! in name {1}".format(z, x + 1))
except ValueError:
    print("Not Found")
else:
    print("OK!!")

# %%
x = [10, 20, 30]

try:
    print(x[3])
except:
    print("not found")
else:
    print("found")
finally:
    print("OK")

# %%
try:
    print("Try")
finally:
    print("Finally")

# %%
name1 = ["choi", "park", "kim", "lee"]

try:
    name1.index("cho")
except ValueError:
    print("ValueError")
except IndexError as V:
    print("IndexError")
except Exception:
    print("Exception")
else:  # 에러가 안나는 경우
    print("else")
finally:  # 무조건 실행
    print("finally")

# %%
try:
    a = "333"
    if a == "kim":
        print("허가!!")
    else:
        raise ValueError
except ValueError:
    print("문제 발생")
except Exception as e:
    print(e)
else:
    print("OK")

# %%
number = int(input("정수입력 : "))

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError
