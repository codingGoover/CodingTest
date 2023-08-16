'''
1697번 숨바꼭질 실버1
insight
    >> 수빈이의 이동 위치를 큐에 저장
       이동 초는 visted 에 표시
문제
https://www.acmicpc.net/problem/1697

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.

반례 모음
https://forward-gradually.tistory.com/53

'''

import sys
from collections import deque
input=sys.stdin.readline

    
visted=[-1]*100001
N,K= map(int,input().split())
queue=deque([N])
visted[N]=0

while queue:
        x= queue.popleft()
        for nx in [-1+x,1+x,x*2]:
            if 0<=nx<=100000 and visted[nx]==-1:
                queue.append(nx)
                visted[nx]=visted[x]+1
                if nx==K:
                    break 

print(visted[K])