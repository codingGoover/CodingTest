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
