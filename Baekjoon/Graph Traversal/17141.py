'''
17141번 연구소2 골드4

>> 바이러스를 퍼트릴 수 있는 위치도 연구소1 문제처럼 조합/백트래킹 으로 구해보려함
   자꾸 풀면서 본질적인 visit = False 일때만 방문한다는 조건을 잊음 
   
입력
첫째 줄에 연구소의 크기 N(5 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

출력
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
예제 출력 1 
5

예제 입력 2 
7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 2 
5

예제 입력 3 
7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 3 
4

예제 입력 4 
7 5
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 4 
3

예제 입력 5 
7 3
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 5 
7

예제 입력 6 
7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 6 
-1

예제 입력 7 
5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1
예제 출력 7 
4

예제 입력 8
5 2
1 1 1 1 1
1 1 2 1 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1
예제 출력 8
0
'''
from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input=sys.stdin.readline

# 연구소 크기 N 바이러스개수 M
N,M= map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(N)]
v_position=[(x,y) for y in range(N) for x in range(N) if graph[y][x]==2]
answer=[]

dx,dy=[-1,1,0,0],[0,0,1,-1]
for p_v_pos in combinations(v_position,M):
    
    g= deepcopy(graph)
    
    # 벽 제외 방문안한곳은 -1 표시
    for i in range(N):
        for j in range(N):
            if g[i][j]==2 or g[i][j]==0:
                g[i][j]=-1
                    
    #queue=deque([(x,y,0) for x,y in p_v_pos])
    queue=deque([])
    for x,y in p_v_pos:
        queue.append((x,y,0))
        g[y][x]=0    # 반례 확인해보니 바이러스를 처음 뿌린 곳은 visit 처리를 안해서 틀렸다. 
        
    while queue:
        x,y,cnt=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[ny][nx]!=1 and g[ny][nx]==-1:  #벽이 아니고 방문 안한 곳이라면 바이러스 퍼짐
                g[ny][nx]=0
                queue.append((nx,ny,cnt+1))
                
                
    flag=True        
    for i in range(N):
        for j in range(N):
            if g[i][j]==-1:
                flag=False
                break
    if flag:
        answer.append(cnt)
        
print( min(answer) if answer else -1)
    
    
        

