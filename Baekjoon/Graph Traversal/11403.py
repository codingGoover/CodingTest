import sys
from collections import deque
input=sys.stdin.readline

# 각 정점마다 방문했는지 visited에 저장하고 간선으로 해당 정점이 연결되어 있다면 check에 1을 기록
# 이때 visited는 각 정점을 방문하면서 방문했는지를 기록해야함
# 그냥 이해 자체가 DFS 방식이 더 쉬움.... 아 왤케 구분을 못하냐

N= int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
visit=[[0]*N for _ in range(N)]

def bfs(x):
    queue=deque()
    queue.append(x)
    check=[0 for _ in range(N)]
    
    while queue:
        q= queue.popleft()
        
        for i in range(N):
            if check[i]==0 and graph[q][i]==1:
                queue.append(i)
                check[i]=1
                visit[x][i]=1
                print(*visit, sep='\n')
                print()

for i in range(N):
    bfs(i)

for i in visit:
    print(*i)
    


# DFS
import sys
input = sys.stdin.readline

# 재귀. 처음에 생각한 이차원배열에 따로 링크 정보 저장하기
def dfs(num):
    for i in graph[num]:
        if visited[i] == 0: # 방문한 적 없다면 방문
            visited[i] = 1 # 방문 체크
            dfs(i)

n = int(input())
graph = [[] for i in range(n)]
for i in range(n):
    nums = list(map(int,input().rstrip().split()))
    for j in range(n):
        if nums[j] == 1: # i에서 j로 가는 간선이 존재한다면
            graph[i].append(j) # 그래프에 추가
            
for i in range(n):
    visited = [0 for i in range(n)] # 방문 체크
    dfs(i) 
    print(*visited)

                