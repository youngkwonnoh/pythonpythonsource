from openpyxl import Workbook

def write_excel_template(filename, sheetname, listdata):
    wb = Workbook()
    
    # default sheet 활성화
    sheet1 = wb.active

    # 컬럼 너비 조절
    sheet1.column_dimensions['A'].width = 70

    # sheet 명 변경
    sheet1.title = sheetname
    
    # 데이터 추가
    for row in listdata:
        sheet1.append(row)

    # 저장
    wb.save("./data/"+filename)

    # 닫기
    wb.close

