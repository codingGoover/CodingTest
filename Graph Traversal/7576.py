'''
7576번 토마토 골드5

insight
    >> 아기상어2 유사문제
	   익은 토마토를 먼저 queue에 넣은후 BFS탐색
	   방문한 곳은 날짜로 저장 <-이전 방문day +1
       프로그램 종료 : sys.exit()
문제
https://www.acmicpc.net/problem/7576

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 1 
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
예제 출력 1 
8

예제 입력 2 
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
예제 출력 2 
-1

예제 입력 3 
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
예제 출력 3 
6

예제 입력 4 
5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
예제 출력 4 
14

예제 입력 5 
2 2
1 -1
-1 1
예제 출력 5 
0

예제 입력 6
4 1
1 0 0 1
예제 출력 6
1
'''
import sys
from collections import deque
input= sys.stdin.readline

def bfs():
    day=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if graph[ny][nx]==0:
                    queue.append((nx,ny))
                    graph[ny][nx]= graph[y][x]+1
                    
        day=graph[y][x]-1
    return day
            
    
dx=[-1,0,1,0]
dy=[0,1,0,-1]

M,N=map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(N)]
queue=deque([])


for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((j,i))

day=bfs()

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            print(-1)
            sys.exit()
print(day)

#print(*graph,sep='\n')