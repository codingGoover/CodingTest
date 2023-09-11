'''
10026번 적록색약 골드5

insight
    >> 문제를 간단하게 볼 필요가 있다
       혼자서 꼬아서 생각 x 
       다른 사람들 코드보니 허무했음
       시간과 메모리가 넉넉했던 문제

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1 
4 3

예제 입력 2
5
RRRRR
RBBBR
RBGBR
RBBBR
RRRRR
예제 출력 2
3 3

예제 입력 3
2
RG
GR
예제 출력 3
4 1
'''

from collections import deque

N= int(input())

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
                # 같은 색상으로 같은 영역인 경우
                if  color == graph[ny][nx]:
                    queue.append((nx,ny))
                    visted[c][ny][nx]=True
                    
                # 현재컬러 R or G & 색약인인 경우  방문컬러가 B가 아니면 같은영역취급
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
            # R or G 
            if not visted[0][i][j]:
                bfs(0,i,j)
                cnt1+=1
            if not visted[1][i][j]:
                bfs(1,i,j)
                cnt2+=1
            
print('%d %d' %(cnt1,cnt2))