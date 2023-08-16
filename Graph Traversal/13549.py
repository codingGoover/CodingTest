'''
13549번 숨바꼭질3 골드5

insight
    >> bfs 큐 푸시 순서는 우선순위를 고려해서 넣어야한다. 
       x*2,x-1,x+1 --> 순간이동(0초) 경우를 먼저 탐색해야함

문제
https://www.acmicpc.net/problem/13549

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
2

힌트
수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.
'''

import sys
from collections import deque
input= sys.stdin.readline
time=[-1]*100001
queue=deque([])

N,K=map(int,input().split())
time[N]=0
queue.append(N)

while queue:
    x=queue.popleft()
    if x==K:
        print(time[x])
        break
    #반복순서 -> 시간이 적을 수록 먼저
    for nx in [2*x,x-1,x+1]:           
        if 0<=nx<=100000 and time[nx]<0:
            if nx==2*x:
                time[nx]=time[x]
            else:
                time[nx]=time[x]+1
            queue.append(nx)

        