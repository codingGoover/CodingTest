'''
숫자 문자열과 영단어 Lv1

문제
https://school.programmers.co.kr/learn/courses/30/lessons/81301

>> 파이썬 문자열 replace(a,b)  --> a를 b로 바꿈 
          str.isnumeric() --> 숫자 형태인지 판별
          str.isalpha() --> 문자 형태인지 판별

'''
word= {"zero":0,"one":1,"two":2,"three" :3,"four" :4,"five" :5,"six" : 6,"seven": 7,"eight":8,"nine":9}

def solution(s):
    answer = 0
    for k,v in word.items():
        s=s.replace(k,str(v))
        #print(s)
        
    answer= int(s)    
    return answer



# 강사 코드 
def solution(s):
    # 앞의 두글자 : (영문자길이,숫자값)
    d={
        'ze':(4,'0'),
        'on':(3,'1'),
        'tw':(3,'2'),
        'th':(5,'3'),
        'fo':(4,'4'),
        'fi':(5,'5'),
        'si':(3,'6'),
        'se':(5,'7'),
        'ei':(5,'8'),
        'ni':(4,'9'),
    }

    answer =''
    while len(s)>0:
        if s[0].isnumeric():  # 숫자형태인지 확인하는 함수   / 문자인지 확인하는 함수 --> isalpha()
            answer+=s[0]
            s=s[1:]
        else:
            answer+=d[s[:2]][1]
            s=s[d[s[:2]][0]:]

    return int(answer)