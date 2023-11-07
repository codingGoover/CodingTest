'''
2573번 빙산 골드4

문제
https://www.acmicpc.net/problem/2573

insight
    >> 변수 실수 visted[startY][startX]=True
       여기를 Y  Y 라고 했다. 28퍼센트에서 계속 틀렸습니다.. 현타..
       변수명 실수를 유의하자. 
       방문한 빙산의 사방면이 바다인지 아닌지 구분
       방문처리 조심해야한다.
입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

예제 입력 1 
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
예제 출력 1 
2

예제 입력 2
5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
예제 출력 2 
0

예제 입력 3 
4 4
0 0 0 0
0 3 1 0
0 1 3 0
0 0 0 0
예제 출력 3 
1

예제 입력 4 
5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
예제 출력 4 
0

예제 입력 5 
5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 10 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
예제 출력 5 
0

예제 입력 6 
7 7
0 0 0 0 0 0 0
0 1 1 0 1 1 0
0 1 9 1 9 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0
예제 출력 6 
2

예제 입력 7 
3 25
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0  
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9 3 9 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
예제 출력 7 
2

'''

import sys
from collections import deque
input=sys.stdin.readline

def bfs(startX,startY):
    queue=deque([(startX,startY)])
    visted[startY][startX]=True
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<M and 0<=ny<N and not visted[ny][nx]:  
                if graph[ny][nx]<=0:
                    graph[y][x] -=1
                elif graph[ny][nx]>0:
                    visted[ny][nx]=True
                    queue.append((nx,ny))
                
    
    return 1
                    

#세로 가로
N,M= map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
year=0
dx,dy=[-1,1,0,0],[0,0,-1,1]

while True:
   
    cnt=0
    visted=[[False]*M for _ in range(N)]
   
    for i in range (N):
        for j in range(M):
            if graph[i][j]>0 and visted[i][j]==False:
                cnt+=bfs(j,i)
                if cnt>=2:
                    print(year)
                    sys.exit()
            
    if cnt==0:
        print(0)
        sys.exit()
        
    year+=1

