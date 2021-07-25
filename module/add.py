def sum(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 없음")
        return
    else:
        result = sum(a, b)
        return result


# 모듈 테스트 시
if __name__ == "__main__":
    print(safe_sum("5", 5))
    print(safe_sum(5, 5))
    print(sum(6, 7))
