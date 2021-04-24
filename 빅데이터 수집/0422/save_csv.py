import csv

with open('top_cities2.csv','w',newline='', encoding="utf-8") as f:
    writer=csv.writer(f)

    writer.writerow(['rank,city,population'])
    writer.writerows([
    ['1', '상하이', '24150000'],
    ['2', '카라치', '2350000'],
    ['3', '베이징', '211516000'],
    ['4', '텐진', '14722100'],
    ['5', '이스탄불', '14160467'],
    ])
