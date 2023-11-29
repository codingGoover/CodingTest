'''
14502번 연구소 골드4

>> 벽을 세울 수 있는 모든 경우를 전부 탐색 해보아야
   풀리는 문제. 벽을 세우는 건 3개를 선택하는 조합 이거나 백트래킹을 사용해 3가지를 중복없이 선택한 경우를 만들면됨

   벽을 세우는 규칙 같은걸 생각하는게 아니라
   완전탐색에 완전탐색이었던 문제다!

문제
https://www.acmicpc.net/problem/14502

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

예제 입력 1 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1 
27

예제 입력 2 
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력 2 
9

예제 입력 3 
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 3 
3

'''
from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline

def bfs():
    global answer
    queue= deepcopy(start)
    g=deepcopy(graph)
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx,ny= x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and g[ny][nx]==0:
                g[ny][nx]=2
                queue.append((nx,ny))
    
    cnt=0
    for gg in g:
        cnt+=gg.count(0)
    #print(cnt)
    answer=max(answer,cnt)
    
    #print(answer)


def make_wall(cnt):
    if cnt==3:
        # 벽이 다세워짐
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                make_wall(cnt+1)
                graph[i][j]=0
                

# 세로 N 가로 M
N,M= map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
start= deque([])
dx,dy=[0,0,-1,1],[-1,1,0,0]
answer=0
wall=[]

for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            start.append((j,i))
       
make_wall(0)
print(answer)


