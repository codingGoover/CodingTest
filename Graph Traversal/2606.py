'''
2606번 바이러스 실버3

문제
https://www.acmicpc.net/problem/2606

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

예제 입력 1 
7
6
1 2
2 3
1 5
5 2
5 6
4 7

예제 출력 1 
4

예제 입력 2
3
2
1 3
2 3

예제 출력 2
2

'''
from collections import deque
import sys
input= sys.stdin.readline


def bfs(graph,node,visted):
    global virus
    
    queue=deque([node])
    # 현재 노드를 방문 처리
    visted[node]=True
    
    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기 
        v=queue.popleft()
        #print(v, end = ' ')
        
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visted[i]):
                queue.append(i)
                visted[i]=True
                virus+=1


cnt= int(input())

# 노드별로 방문 정보를 리스트로 표현
visted=[False]*(cnt+1)
graph=[[] for _ in range(cnt+1)]

edge = int(input())
for _ in range(edge):
    v1,v2= map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

virus=0

bfs(graph,1,visted)
print(virus)
