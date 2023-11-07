'''
2589번 보물섬 골드5

문제
https://www.acmicpc.net/problem/2589

insight
    >> pypy3로 하면 된다. 시간초과 화난다
       max 함수 활용 잘하자 (이차원리스트에서, 두 수를 비교)
       시작지점에서 가장 멀리떨어진 지점 거리를 기억하고 각 시작지점 별 최대거리를 비교 후 정답
       bfs: 첫방문이 최소 거리이다
       
입력
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

출력
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

예제 입력 1 
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
예제 출력 1 
8

예제 입력 2
5 5
LLLLL
LWWWL
LWWWL
LWWWL
LLLLL
예제 출력 2
8

예제 입력 3
3 3
LLW
WWW
WWW
예제 출력 3
1

예제 입력 4
1 2
LL
예제 출력 4
1

예제 입력 5
3 3
LLW
WWW
WWW
예제 출력 5
1

예제 입력 6
7 7
WLLLLLW
LWLWLWW
LLLWLWW
LWWWLWW
LLLLLWW
LWWWWWW
WWWWWWW
예제 출력 6
10

예제 입력 7
4 4
LLLL
LLLL
LLLL
LLLL
예제 출력 7
6

예제 입력 8
7 7
LLLWLLL
LLLWLLL
LLWWLLL
WWWWLLL
WWWWWWW
WWWWWWW
WWWWWWW
예제 출력 8
5
'''

import sys
from collections import deque


def bfs(startY,startX):
    
    visted[startY][startX]=0
    queue= deque([(startX,startY)])

    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<M and graph[ny][nx]=='L' and visted[ny][nx]==-1 :
                visted[ny][nx]=visted[y][x]+1
                queue.append((nx,ny))
                        
    return max(map(max,visted))
   

#세로 가로
M,N= map(int,input().split())
graph=[list(input()) for _ in range(M)]
shortest=0
dx,dy=[-1,1,0,0],[0,0,-1,1]

for i in range(M):
    for j in range(N):
        if graph[i][j]=='L':
            visted=[[ -1 for _ in range(N)] for _ in range(M)]
            shortest=max(shortest,bfs(i,j))
           
print(shortest)

