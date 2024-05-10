import random as r
import time

## 범위
min = 1
max = 46

## 사용자가 입력한 번호를 저장할 변수
user = []

## 발급된 로또 번호가 저장될 변수
lotto = []

## 사용자에게 입력받는 값의 유효성을 검사하는 함수        
msg = ''
def inputNumber():
    try :
        num = int(input('번호를 입력하세요 >> '))
        if(min<=num<max):
            return num
        print('1~45사이의 숫자만 입력하세요')
        return inputNumber()
    except : 
        print('1~45사이의 숫자만 입력하세요')
        
## 몇개를 맞췄는지 확인하는 함수
def matchCnt():
    count = 0
    for i in user:
        if(i in lotto):
            count+=1
    return count

## 맞춘개수에 따라 등수를 출력하는 함수
def result(count):
    if(count == 6) :
        return '1등'
    elif(count == 5) :
        return '2등'
    elif(count == 4) :
        return '3등'
    else :
        return '낙첨'

## 로또 번호 발급
while True:
    ## 종료조건
    if(len(lotto)==6):
        break
    num = r.randint(min, max)
    if(num in lotto) :
        continue
    else :
        lotto.append(num)

def printlotto():
    print(lotto)

## 사용자가 번호를 입력
def startlotto():
    while True:
        ## 종료조건
        if(len(user)==6):
            ## 결과를 보여줄 함수
            print(result(matchCnt()))
            print(time.strftime('%Y년 %m월 %d일',time.localtime(time.time()))+' 당첨번호는 ' + str(lotto) + '입니다')
            break
        userNum = inputNumber()
        if(userNum in user) :
            print('이미 선택한 번호입니다 다시 입력하세요')
            continue
        else :
            user.append(userNum)
