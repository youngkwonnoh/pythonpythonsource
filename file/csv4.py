# 2차원 리스트 => csv에 저장
import csv

list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

with open("./data/numbers1.csv", "w") as f:
    writer = csv.writer(f)

    for row in list1:
        writer.writerow(row)