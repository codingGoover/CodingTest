'''
13913번 숨바꼭질4 골드4

문제
https://www.acmicpc.net/problem/13913

insight
    >> queue 원소 단위는 튜플로 묶어줘야한다 ([a,b,c])
       리스트 append --> return 값은 원소추가된 리스트가 아니라 아무것도 없다 none
       x-1 경로로 밖에 가지 못하는 경우(예: 1000 0)는 내림차순 출력으로 따로 처리함 

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17

예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17

반례모음
https://forward-gradually.tistory.com/72

'''

import sys
from collections import deque
import time
input=sys.stdin.readline

def append(list,dx):
    newlst=list[:]
    newlst.append(dx)
    return newlst

visted=[False]*100001
N,K= map(int,input().split())

#수빈위치, 시간, 경로
queue=deque([(N,0,[N])])


#100000 0 같은 경우 내림차순 출력 
if N>K:
    print(N-K)
    for n in range(N,K-1,-1):
        print(n, end=' ')
    sys.exit()
    
while queue:
    x,time,route=queue.popleft()
    visted[x]=True
    if x==K:
        print(time)
        print(*route,sep=' ')
        break

    for dx in (x-1,x+1,2*x):
        if 0<=dx<=100000 and not visted[dx]:
            queue.append((dx,time+1,append(route,dx)))


