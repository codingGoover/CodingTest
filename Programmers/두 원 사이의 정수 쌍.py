'''
두 원 사이의 정수 쌍 Lv2

문제
https://school.programmers.co.kr/learn/courses/30/lessons/181187?language=python3

insight
    >> 수학적으로 생각하면 쉬운 문제이나 생각이 안나면 답이 없다
       math 라이브러리 내장함수 이용
       파이썬은 math.sqrt(음수) --> ValueError

참고 
https://aram-su.tistory.com/21

테스트 케이스 1
2 3 
20

테스트 케이스 2
1 3 
28

테스트 케이스 3
2 4
40

테스트 케이스 4
9 20
1008

테스트 케이스 5
10 20
952

테스트 케이스 6
999999 1000000
6281440

'''
import math

def solution(r1, r2):
    answer=0
    
    for i in range(1,r2+1):   
        y2=math.sqrt(math.pow(r2,2)-math.pow(i,2))
        
        if i>r1:
            y1=0
        else:
            y1= math.sqrt(math.pow(r1,2)-math.pow(i,2))
         
        answer+=(math.floor(y2)-math.ceil(y1)+1)
        
    answer*=4
    
    return answer