import openpyxl

excel_file = openpyxl.load_workbook("./data/sample.xlsx")
print(excel_file)
print(type(excel_file))
print(excel_file.sheetnames)

# sheet 가져오기
sheet1 = excel_file['영업사원매출']

# sheet1['D18'].value

for item in sheet1.rows:
    print(item[0].value, item[1].value, item[2].value, item[3].value, item[4].value, item[5].value, item[6].value)