import requests
from bs4 import BeautifulSoup
import csv

def crawl_table_data(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # <table> 요소 선택
    table_element = soup.select_one("table")

    # 추출한 데이터를 저장할 리스트 생성
    data = []

    # <table> 내부의 행(tr)을 순회하며 데이터 추출
    for row in table_element.select("tr"):
        row_data = [cell.get_text(strip=True) for cell in row.select("td")]
        if row_data:
            data.append(row_data)

    return data

# 크롤링할 페이지 URL
url = "https://lgbeatsamsung.com/admin/starpeoplelist.html?ordertype=&mode=&cate=&keyword=&page=1"

# 사이트의 table 데이터 크롤링
result = crawl_table_data(url)

# 데이터를 CSV 파일로 저장
filename = "table_data.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(result)

print(f"Data has been saved to {filename}.")