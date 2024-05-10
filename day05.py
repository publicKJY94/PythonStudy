## 파일 입출력
## 파이썬 언어 특성상, 파일을 읽어들이는 경우가 매우 많음
## 데이터 => 파일 => 분석, 가공, 시각화

## 파일을 읽어들이는 코드
##file=open('test.txt','rt')
##while True:
##    file.readline()
##    if(file):
##file.close()

## wt : write text : 덮어쓰기 > 원본손상
## at : add text : 이어쓰기
count = 0
answer = ''
ask = ''

with open('quiz.txt','rt') as rfile:
    answer = rfile.readline()
    for i in range(len(answer)):
        ask+='_'

def printMsg(spel, ask):
    temp = ''
    for i in range(len(answer)):
        if(answer[i] == spel):
            temp += spel
        else :
            temp += ask[i]
    ask = temp
    return ask
           
print(ask)
while True:
    msg = input('입력 >> ')
    ask = printMsg(msg[0], ask)
    print(ask)
    count+=1
    if(answer == ask):
        print(count)
        with open('quiz.txt','at') as wfile:
            wfile.write('\n'+str(count)+'번만에 맞추셨습니다')
        break
