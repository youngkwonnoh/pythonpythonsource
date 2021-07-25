from openpyxl import Workbook

# 객체 생성
wb = Workbook()

# 엑셀 파일이 생성될 때 기본 시트가 하나 존재
# 기본 시트를 활성화
ws1 = wb.active

# ws1 가리키는 시트명 변경
ws1.titel = "range names"

for row in range(1, 40):
    ws1.append(range(600))

# 시트 생성
ws2 = wb.create_sheet(title="Data")
ws2["F5"] = 3.14



# 파일 작성
wb.save("./data/test1.xlsx")