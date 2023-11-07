'''
1260번 DFS와 BFS 실버2

insight
    >> dfs 익히기
       이문제의 포인트는 정점 번호가 작은 것을 먼저 방문한다

문제
https://www.acmicpc.net/problem/1260

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4

예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5

예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999

'''
import sys
from collections import deque
input= sys.stdin.readline

def bfs(start):
    visted[start]=True
    queue=deque([start])
  
    while queue:
        x=queue.popleft()
        print(x,end=' ')
        for nx in graph[x]:
            if not visted[nx]:
                queue.append(nx)
                visted[nx]=True

def dfs(start):
    visted[start]=True
    print(start,end=' ')
     
    for x in graph[start]:
        if not visted[x]:
            dfs(x)
    

#정점개수, 간선개수, 탐색시작번호
N,M,V= map(int,input().split())


graph=[[]for _ in range(N+1)]

for _ in range(M):
    x1,x2= map(int,input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)

# "단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문"
# --> 그래프 저장순서를 오름차순으로 정렬
for i in range(1,N+1):
    graph[i].sort()

visted=[False]*(N+1)
dfs(V)
print()

visted=[False]*(N+1)
bfs(V)
    


