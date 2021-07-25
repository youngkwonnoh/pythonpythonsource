from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()

# default sheet 활성화
sheet1 = wb.active

# 데이터 추가
# 제목 행
sheet1.append(['이름', '생년월일', '이미지'])

# 데이터 행 추가
rows = [
    ['홍길동', '801020'],
    ['송혜교', '851115'],
    ['김지원', '860912'],
    ['남주혁', '880705'],

]

for idx, row in enumerate(rows, 2):
    sheet1.append(row)
    img = Image("./data/tent1.jpg")
    img.width = 30
    img.height = 30
    sheet1.add_image(img, 'C'+str(idx)) # C2, C3


wb.save("./data/test3.xlsx")