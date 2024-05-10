import csv

# 2018년도 0~9세 가장 적은 지역
# 2018년도와 2023년도를 비교했을때,
# 0~9세 인원의 감소율이 20%미만인 지역의 이름을 모두 출력해주세요.
area = []
with open('gathering.csv','r') as file :
    data=csv.reader(file)
    header = next(data)
    pivot = next(data)
    for row in data :
        row[3] = int(row[3].replace(',',''))
        row[-11] = int(row[-11].replace(',',''))
        if (row[-11]/row[3]*100)>80 :
            area.append(row[0].split(' ')[2])
print(area)
