# csv 파일 읽기
import csv

with open("./data/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")

    for c in reader:
        print(c)