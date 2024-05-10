## 문자열을 저장할 리스트
li = []
## a가 가장 많은 문자열을 담을 변수
keyword = ''
## a로 시작하는 문자열의 개수를 카운트
acount = 0
while True:
    word = input('단어를 입력하세요 >> ')
    ## equals()가 적용 불가...?
    if(word == 'stop') :
        break
    if word.startswith('a'):
    ## 증감연산자가 사용 불가능..
        acount = acount+1; 
        ## a의 개수가 동일하다면 변경이 일어나지 않아야 하기 때문에 등호가 없이
        if(word.count('a') > keyword.count('a')):
            keyword = word
    li.append(word)
print('a로 시작하는 단어의 개수 : ' + str(acount))
print('a가 가장 많이 포함된 문자열 : ' + keyword)
