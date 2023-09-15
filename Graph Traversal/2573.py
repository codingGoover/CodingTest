import sys
from collections import deque
input=sys.stdin.readline

def bfs(startY,startX):
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
                cnt+=bfs(i,j)
                #print('x %d y %d'%(j, i))
                #print('cnt= %d'%cnt)
                #print('year= %d'%year)
                
    if cnt>=2:
        print(year)
        sys.exit()
        
    if cnt==0:
        print(0)
        sys.exit()
        
    year+=1

