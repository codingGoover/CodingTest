'''
7569번 토마토 골드5
insight
	>> 토마토 3차원 배열 문제. dz 필요
	   return 하는 day 변수 초기화 필수! 
	   UnboundLocalError: local variable 'day' referenced before assignment 런타임에러 발생

문제
https://www.acmicpc.net/problem/7569

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

예제 입력 1 
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
예제 출력 1 
-1

예제 입력 2 
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
예제 출력 2 
4

예제 입력 3 
4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
예제 출력 3 
0

예제 입력 4
4 4 1
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
예제 출력 4
-1

'''
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    day=0
    while queue:
        x,y,z=queue.popleft()
        for dx,dy,dz in [(0,0,1),(0,1,0),(1,0,0),(0,0,-1),(0,-1,0),(-1,0,0)]:
            nx=x+dx
            ny=y+dy
            nz=z+dz
            
            if 0<=nx<M and 0<=ny<N and 0<=nz<H:
                if graph[nz][ny][nx]==0:
                    graph[nz][ny][nx] = graph[z][y][x]+1
                    queue.append((nx,ny,nz))
        
        day= graph[z][y][x]-1
        
    return day        

M,N,H= map(int,input().split())
graph=[[list(map(int,input().split())) for _ in range(N)]for _ in range(H)]
queue= deque([])

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x]==1:
                queue.append((x,y,z))

day= bfs()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x]==0:
                print(-1)
                sys.exit()
                
print(day)

#print(*graph,sep='\n')