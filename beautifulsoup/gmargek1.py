import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

# 엑셀 저장 준비
wb = Workbook()

# 기본 시트 활성화
sheet1 = wb.active
sheet1.tlte = "컴퓨터/전자베스트100"

# 컬럼 너비 조절
sheet1.column_dimensions['B'].width = 30
sheet1.column_dimensions['C'].width = 80
sheet1.column_dimensions['D'].width = 75
sheet1.column_dimensions['E'].width = 20

# 제목 행 추가
sheet1.append(['번호', '회사명', '제품명', '상세정보url', '가격'])







url = "http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06"

# 제품명, 가격

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# best-list 클래스명을 가진 요소가 2개 추출
best_list = soup.select("div.best-list")[1]
# 제품 목록 추출
best_list_li = best_list.select("ul > li")
# print(bets_list_li)

for idx, item in enumerate(best_list_li, 1):
    # 제품명 추출
    product_name = item.select_one("a.itemname")
    # 제품 가격 추출
    product_price = item.select_one("div.s-price span")
    
    # url을 이용하여 회사정보 추출
    product_company_response = requests.get(product_name['href'])
    soup = BeautifulSoup(product_company_response.content, 'html.parser')
    
    # 회사명 추출
    product_company = soup.select_one("span.text")

    # AttributeError: 'NoneType' object has no attribute 'text'
    # 정보가 없을 때
    if product_company:
        product_company = product_company.text
    else:
        product_company = soup.select_one('span.text__seller > a').text
    # 확인
    # print(idx, product_company, product_name.text, product_price.text, product_name['href'])
    # ['번호', '회사명', '제품명', '상세정보url', '가격']
    sheet1.append([idx, product_company, product_name.text, product_name['href'], product_price.text])

    # 하이퍼링크 걸어주기
    sheet1.cell(row=idx+1, column=4).hyperlink = product_name['href']

# 서식 지정하기
cell_A1 = sheet1['A1']
cell_A1.alignment = Alignment(horizontal='center')
cell_A1.font = Font(color="01579B")

wb.save("./data/gmarket_best100.xlsx")


