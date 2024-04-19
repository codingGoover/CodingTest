'''
2583번 영역 구하기 실버1

문제
https://www.acmicpc.net/problem/2583

'''

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)   #이거 안붙여서 런타임 에러남 


dx,dy=[0,0,-1,1],[-1,1,0,0]

#세로,가로
M,N,K=map(int,input().split())
rect=[list(map(int,input().split()))for _ in range(K)]
board=[[0]*N for _ in range(M)]
ans=[]


def dfs(y,x):
    global sum
    #print(sum)
    board[y][x]=1
    
    for i in range(4):
        ny,nx= y+dy[i], x+dx[i]
        if 0<=ny<M and 0<=nx<N and  board[ny][nx]==0:
            board[ny][nx]=1
            sum+=1
            dfs(ny,nx)
    

for r in rect:
    x1,y1,x2,y2=r[0],r[1],r[2],r[3]
    
    for y in range(y1,y2):
        for x in range(x1,x2):
            board[y][x]=1
    
for y in range(M):
    for x in range(N):
        if board[y][x]==0:
            sum=1
            dfs(y,x)
            ans.append(sum)

print(len(ans))
print(*sorted(ans))



# bfs 방식 이게 좀 더 간단함 왜 bfs로 먼저 접근을 못했지?
# 아예 큐 시작점을 dfs처럼 남은 영역별 따로 따로 해주면 간단하다고 느낌
 
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global answer
    queue = deque()
    queue.append((x, y))
    board[x][y] = 1
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny))
                size += 1
    result.append(size)

result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            bfs(i, j)
            
result.sort()
print(len(result))
for i in result:
    print(i, end=' ')