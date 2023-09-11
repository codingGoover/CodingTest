from collections import deque


N= int(input())
'''
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''
def bfs(c,b,a):
    visted[c][b][a]=True
    color= graph[b][a]
    
    queue= deque([(a,b)])
    
    while queue:
        x,y= queue.popleft()
        
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visted[c][ny][nx]:
                
                if  color == graph[ny][nx]:
                    queue.append((nx,ny))
                    visted[c][ny][nx]=True
                    
                elif color!='B' and c==1 :
                    if graph[ny][nx]!='B':
                        queue.append((nx,ny))
                        visted[c][ny][nx]=True
                
                
                    


graph=[list(input()) for _ in range(N)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
visted=[[[False for _ in range(N)]for _ in range(N)]for _ in range(2)]
cnt1,cnt2=0,0

for i in range (N):
    for j in range(N):
              
        if  graph[i][j]=='B':
            if not visted[0][i][j]:
                bfs(0,i,j)
                cnt1+=1
                cnt2+=1
        else:
            if not visted[0][i][j]:
                bfs(0,i,j)
                cnt1+=1
            if not visted[1][i][j]:
                bfs(1,i,j)
                cnt2+=1
            
print('%d %d' %(cnt1,cnt2))