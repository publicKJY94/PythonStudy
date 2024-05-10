## 파이썬에서 다루는 데이터파일 등은 대부분 .csv를 의미하는 것

import csv

##with open('weather.csv', 'rt') as file :
##    ## delimiter -> ~을 기준으로 구별한다
##    reader = csv.reader(file, delimiter=',')
##    for line in reader :
##        print(line)
        
## 파일에서 읽는 데이터의 자료형은 문자열이다

## 줄 바꿈현상이 발생하는 것을 억제하기 위해 newlines를 넣어준다
##with open('test.csv','at', newline='') as file :
##    writer = csv.writer(file, delimiter=',')
##    writer.writerow([11,'레오나'])
##    writer.writerow([12,'징크스'])
##    
##li = []
## 기상청 csv 파일을 불러와서
## 가장 8월의 평균온도가 높았던 년도를 알려주세요.
##with open('weather.csv', 'rt') as file :
##    reader = csv.reader(file, delimiter=',')
##    for line in reader :
##        if line[2][:-2] == '08' :
##            li.append(line[2][:4])
##            li.append(line[3])

maxTemp=0
date=''
with open('weather.csv','r') as file :
    data=csv.reader(file)
    header = next(data)
    for row in data :
        row[5]=float(row[5])
        if maxTemp < row[5] :
            maxTemp=row[5]
            date=row[-4]


