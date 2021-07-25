import re
import openpyxl

# 엑셀 파일 가져오기
wb = openpyxl.load_workbook("./regex/train.xlsx")

# 현재 활성화 된 시트 가져오기
sheet1 = wb.active

# 성별 추출
# pattern = re.compile(" [A-Za-z]+\.")  # Mr. or Miss. or Mrs.

# 남자 추출
pattern = re.compile(" Mr\.")

for row in sheet1.rows:
    # print(row[3].value)  # 이름 열을 읽어오기
    # print(pattern.findall(row[3].value))
    gender_m = pattern.findall(row[3].value)  # [] or [' Mr. ']
    if gender_m:
        print(row[3].value)
