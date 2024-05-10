## 사용자 정의 함수

## 함수 3 요소
## 1) input 입력값 인자 인수 매개변수 parameter argument
## 2) output 출력값 결과값 return 반환
## 3) 기능 ▶ 함수명

## 선언(정의) != 호출

## 유형 1
def hello():
    pass # 함수 미완성

## 유형 2
def printMessage(name,msg='기본 메세지'): # 기본 인자(디폴트 인자) : JAVA의 오버로딩을 가능하게 함
    print(name+'님의 메세지 : '+msg)

def printInfo(*args): # 가변 인자 → 튜플(변화를 허용하지않는 리스트)
    print(type(args))
    print(args)
    for v in args :
        print(v)

## 유형 3
def makeNum():
    num=1234
    return num


def makeAvg(li):
    return round(sum(li)/len(li),1)

def makeSum(li):
    return sum(li)
    
def inputScore():
    li=[]
    while True:
        grade = int(input('정수입력 >> '))
        if(grade<0):
            break
        li.append(grade)
##    printSumAvg(li)
    return makeSum(li), makeAvg(li)
