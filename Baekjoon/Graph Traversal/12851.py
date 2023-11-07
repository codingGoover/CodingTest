'''
12851번 숨바꼭질2 골드4

문제
https://www.acmicpc.net/problem/12851

insight
    >> "트리" BFS 문제 ? 트리의 LEVEL이 존재 (=시간 time)
       너비우선 탐색 중 같은 레벨에서 방문 처리에 따라 트리가 펼쳐지는 유무가 결정된다.
       1 + 1 =2  vs 1 * 2 = 2
       같은 2 값이지만 다른 경우로 취급함. 최소 레벨의 2 가 모두 나타나야한다. (=큐에 push되어야함)
       push 방문 처리 --> 한번의 방문으로 방문처리됨. 같은 레벨에서 다시 나와도 (=도착 방법이 다름) 방문 불가능함
       pop  방문 처리 --> 큐에 최소 시간때로 가능한 위치(숫자)가 모두 들어가지고, pop후 방문처리 하므로 다음 레벨부터 방문이 불가능함  
       
       ∴ 도착 최소시간이 아닌 방법의 가지수를 묻는 문제이므로 pop 시 방문처리!
       
    
입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
2

반례 질문게시판
https://www.acmicpc.net/board/view/56215

 
'''

import sys
from collections import deque
input=sys.stdin.readline

N,K= map(int,input().split())
queue= deque([(N,0)])
visted=[False]*1000001
ans=0
cnt=0

while queue:
    x,time=queue.popleft()
    visted[x]=True
    
    if cnt>0:
        if time==ans and x==K: 
            cnt+=1
    elif cnt==0 and x==K: 
        ans=time
        cnt+=1
    else:    
        for dx in (x-1,x+1,2*x):
            if 0<=dx<=100000 and not visted[dx]:
                queue.append((dx,time+1))
        

print(ans)
print(cnt)