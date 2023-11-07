import sys
from collections import deque
input= sys.stdin.readline

'''
1325번 효율적인 해킹 실버1

insight
    >> pypy의 존재란 무엇일까.. 
       시간초과라는 걸림돌. 
       A → B  vs B → A 
       아무튼 B와 연결된 노드를 카운트할줄 알아야함

문제
https://www.acmicpc.net/problem/1325

질문게시판
https://www.acmicpc.net/board/view/123040

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

예제 입력 1 
5 4
3 1
3 2
4 3
5 3
예제 출력 1 
1 2

예제 입력 2
3 3
1 2
2 1
1 3
예제 출력 2
3

'''


#A → B
#A를 방문해서 노드와 연결된 B들을 카운트 
def bfs(node):
    queue=deque([node])
    visted=[True if i==node else False for i in range(N+1)]
    
    while queue:
        cur= queue.popleft()
        for x in graph[cur]:
            if not visted[x]:
                queue.append(x)
                visted[x]=True
                cnt[x]+=1
    
N,M= map(int,input().split())
graph= [[]for _ in range(N+1)]
cnt=[0]*(N+1)

for _ in range(M):
    A,B= map(int,input().split())
    graph[A].append(B)


for i in range(1,N+1):
    bfs(i)
    
ans= max(cnt)
answer=[index for index, val in enumerate(cnt) if val==ans]
print(*answer, sep=' ')



#B → A  
#B를 방문해서 그 노드에 연결된 컴퓨터수를 한번의 bfs로 카운트
def bfs(node):
    queue=deque([node])
    visted=[True if i==node else False for i in range(N+1)]
    cnt=0
    
    while queue:
        cur= queue.popleft()
        for x in graph[cur]:
            if not visted[x]:
                queue.append(x)
                visted[x]=True
                cnt+=1
    
    return cnt

N,M= map(int,input().split())
graph= [[]for _ in range(N+1)]
cnt=[0]*(N+1)

for _ in range(M):
    A,B= map(int,input().split())
    graph[B].append(A)


for i in range(1,N+1):
    cnt[i]=bfs(i)

ans= max(cnt)
answer=[index for index, val in enumerate(cnt) if val==ans]
print(*answer, sep=' ')