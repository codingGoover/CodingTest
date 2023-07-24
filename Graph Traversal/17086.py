'''
17086번 아기상어2 실버2

insight
    >> 처음푼 최단경로 문제
       미리 도착점을 queue에 넣어두고 다른 출발가능 지점들로 BFS탐색
       최소->최소값을 저장하기에 방문의 유무만이 곧 최소값을 걸러내는 것

문제
https://www.acmicpc.net/problem/17086

입력
첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다. 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

출력
첫째 줄에 안전 거리의 최댓값을 출력한다.

예제 입력 1 
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
예제 출력 1 
2

예제 입력 2 
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
예제 출력 2 
2

예제 입력3
1 3
1 0 0
예제 출력3
2

예제 입력4
4 2
1 0
0 0
0 0
0 1
예제 출력4
1
'''
import sys
from collections import deque
input= sys.stdin.readline

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx= x+dx[i]
            ny= y+dy[i]
            
            if 0<=nx<M and 0<=ny<N:
                if graph[ny][nx]==0:
                    graph[ny][nx]=graph[y][x]+1
                    queue.append((nx,ny))
                    
                    

dx=[0,0,-1,1,-1,-1,1,1]
dy=[1,-1,0,0,1,-1,-1,1]

N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
queue= deque([])

for i in range (N):
    for j in range (M):
        if graph[i][j]==1:
            queue.append((j,i))
            
bfs()

print(max(map(max,graph))-1)
