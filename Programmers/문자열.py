'''
실습문제01
QR code Lv0 

문제
https://school.programmers.co.kr/learn/courses/30/lessons/181903

>> in enumerate() 문법 헷갈렸음

'''
def solution(q, r, code):
    answer = ''
    for idx,c in enumerate(code):
        #print(idx, c)
        if idx%q==r:
            answer+=c
    return answer


'''
실습문제02
크기가 작은 부분 문자열 Lv1 

문제
https://school.programmers.co.kr/learn/courses/30/lessons/147355

입출력 예
t	p	result
"3141592"	"271"	2
"500220839878"	"7"	8
"10203"	"15"	3


입출력 예 #2
p의 길이가 1이므로 t의 부분문자열은 "5", "0", 0", "2", "2", "0", "8", "3", "9", "8", "7", "8"이며 이중 7보다 작거나 같은 숫자는 "5", "0", "0", "2", "2", "0", "3", "7" 이렇게 8개가 있습니다.

입출력 예 #3
p의 길이가 2이므로 t의 부분문자열은 "10", "02", "20", "03"이며, 이중 15보다 작거나 같은 숫자는 "10", "02", "03" 이렇게 3개입니다. "02"와 "03"은 각각 2, 3에 해당한다는 점에 주의하세요
'''
def solution(t, p):
    answer = 0
    l= len(p)

    for i in range(len(t)-l+1):
        temp=t[i]
        for j in range(1,l):
            temp+=t[i+j]
       
        #print(temp)
        if int(temp)<=int(p):
            answer+=1
        
    return answer



'''
실습문제03
문자열 겹쳐쓰기 Lv0 

문제
https://school.programmers.co.kr/learn/courses/30/lessons/181943

입출력 예
my_string	overwrite_string	s	result
"He11oWor1d"	"lloWorl"	2	"HelloWorld"
"Program29b8UYP"	"merS123"	7	"ProgrammerS123"

'''
def solution(my_string, overwrite_string, s):
   
    #방법1
    for i in range(len(my_string)):
        if s<=i<s+len(overwrite_string):
            answer+=overwrite_string[i-s]
        else:
            answer+=my_string[i]
       
     
    #방법2   
    lst=list(my_string)
    for i in range(s,s+len(overwrite_string)):
        lst[i]=overwrite_string[i-s]
    answer=''.join(lst)
    
    #방법3
    #슬라이싱을 시도하면 문자열의 범위를 초과하더라도 빈값이 return되고 에러는 나지 않는다.
    answer=my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    
    return answer
 