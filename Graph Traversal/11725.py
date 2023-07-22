'''
11725번 트리의 부모 찾기 실버2

문제
https://www.acmicpc.net/problem/11725

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7

예제 출력 1 
4
6
1
3
1
4

예제 입력 2 
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12

예제 출력 2 
1
1
2
3
3
4
4
5
5
6
6

예제 입력3
3
2 3
1 2

예제 출력3
1
2

예제 입력4
10
1 3
5 4
3 2
2 7
5 7
9 10
5 10
6 8
1 6

예제 출력4
3
1
5
7
1
2
6
10
5

insight
>> 새로 방문한 곳에서 연결된 노드 검사시 from노드를 찾으면 그것이 부모이다. 
   == 곧 자식노드에서 연결된 노드들 중 이미 방문했던 곳이면 부모노드임.
   
'''

from collections import deque
import sys
input=sys.stdin.readline

def bfs(graph,visted,node):
    visted[node]=True
    queue=deque([])
    queue.append(node)
    
    while queue:
        now_node=queue.popleft()
        
        for v in graph[now_node]:
            if visted[v]==False:
                queue.append(v)
                visted[v]=True
            else:
                parent[now_node]=v
 



N= int(input())
visted=[False]*(N+1)
parent=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(N-1):
    v1,v2= map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
bfs(graph,visted,1)

for p in parent[2:]:
    print(p)
