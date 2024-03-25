'''
1205번 등수 구하기 실버4

insight
>> 단순 구현문제
   상황에 따른 케이스 분류 필요
   입력 범위도 작음

'''

import sys
input=sys.stdin.readline

N,S,P=map(int,input().split())
score=[]
if N>0:
    score=list(map(int,input().split()))

# 랭킹리스트가 적은 경우 무조건 추가가능

if N>=P and score[-1]>=S:
    print(-1)
else:
    top=0
    for s in score:
        if s>S:
            top+=1
    print(top+1)
