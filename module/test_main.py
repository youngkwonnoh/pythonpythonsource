import test

number = test.number_input()

print("둘레 : ", test.get_circumference(number))
print("넓이 : ", test.get_circle_area(number))


print(">> test_main 의 __name__ 출력")
print(__name__)