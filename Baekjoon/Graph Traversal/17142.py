'''
17142번 연구소3 골드3

>> 문제 이해가 모호했던 문제. 활성/비활성 바이러스의 설명이 부족했다고 생각함
   비활성 바이러스로 남아있어도, 바이러스이기 때문에 더 퍼뜨리지 않아도 된다. 
   바이러스로 만들어야하는 빈칸 개수를 체크해 비활성바이러스를 더 활성으로 만들지 않아도 되는 경우 처리를 함
   다 구하고 마지막에 max time을 구함
   
   다른사람 코드? 
   모든 칸에 바이러스가 퍼지는 최소 시간을 구할 때, 활성 상태 바이러스가 비활성 상태인 바이러스 자리까지 도달하는 데에 걸리는 시간은 고려하지 않음, 
   즉. time을 갱신할 때에는 활성 상태에서만 고려해야함  --> 내 코드에서 해보려했는데 틀렸습니다 뜸 
   
입력
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

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
4

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
4

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
0

예제 입력 8
4 1
1 1 1 1
0 2 2 0
1 1 1 1
1 1 1 1
예제 출력 8
2
'''

from collections import deque
from copy import deepcopy
from itertools import combinations
import sys
input=sys.stdin.readline

# 연구소 크기 N     활성 가능 바이러스 개수 M
N,M= map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(N)]
v_position= [(x,y) for y in range(N) for x in range(N) if graph[y][x]==2]
dx,dy=[0,0,-1,1],[-1,1,0,0]
answer=[]

# for p_v_position in combinations(v_position,M):
#     #[(x,y) ,(x1,y2), (x2,y2)]
#     visit= deepcopy(graph)
#     cnt=0
#     for i in range(N):
#         for j in range(N):
#             if visit[i][j]==0: 
#                 visit[i][j]=-1
#                 cnt+=1
#             elif visit[i][j]==1: #벽이면
#                 visit[i][j]='-'
#             elif visit[i][j]==2: #비활성 바이러스라면
#                 visit[i][j]='*'
                
#     queue=deque([])
#     for x,y in p_v_position:
#         queue.append((x,y))
#         visit[y][x]=0
    
#     while queue:
#         x,y=queue.popleft()
#         if cnt==0:
#             break
        
#         for i in range(4):
#             nx,ny=x+dx[i],y+dy[i]
#             if cnt>0 and 0<=nx<N and 0<=ny<N:
#                 if visit[ny][nx]==-1:
#                     #print(f'x:{x} y:{y} nx:{nx} ny:{ny}')
#                     visit[ny][nx]=visit[y][x]+1
#                     cnt-=1
#                     queue.append((nx,ny))
#                 elif visit[ny][nx]=='*':
#                     #print(f'x:{x} y:{y} nx:{nx} ny:{ny}')
#                     visit[ny][nx]=visit[y][x]+1
#                     queue.append((nx,ny))
        
        
        
#     #print(*visit,sep='\n')
#     #print()
#     ans=-1
#     if cnt==0:
#         for i in range(N):
#             for j in range(N):
#                 if visit[i][j]!='*' and visit[i][j]!='-':
#                     ans=max(ans,visit[i][j])
#         answer.append(ans)
#         #print(ans)
#         #print(answer)  
    


def bfs(p_v_position):
    visit= deepcopy(graph)
    cnt=0
    
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0: 
                visit[i][j]=-1
                cnt+=1
            elif visit[i][j]==1: #벽이면
                visit[i][j]='-'
            elif visit[i][j]==2: #비활성 바이러스라면
                visit[i][j]='*'
                
    queue=deque([])
    for x,y in p_v_position:
        queue.append((x,y))
        visit[y][x]=0
    
    while queue:
        x,y=queue.popleft()
        
        if cnt==0:
            break
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if cnt>0 and 0<=nx<N and 0<=ny<N:
                if visit[ny][nx]==-1:
                    #print(f'x:{x} y:{y} nx:{nx} ny:{ny}')
                    visit[ny][nx]=visit[y][x]+1
                    cnt-=1
                    queue.append((nx,ny))
                elif visit[ny][nx]=='*':
                    #print(f'x:{x} y:{y} nx:{nx} ny:{ny}')
                    visit[ny][nx]=visit[y][x]+1
                    queue.append((nx,ny))
        
        
        
    #print(*visit,sep='\n')
    #print()
    ans=-1
    if cnt==0:
        for i in range(N):
            for j in range(N):
                if visit[i][j]!='*' and visit[i][j]!='-':
                    ans=max(ans,visit[i][j])
        answer.append(ans)
        #print(ans)
        #print(answer)  


# 질문 게시판 보다가 bfs를 함수로 처리하면 시간초과 X --> 진짜임 
# 똑같은 코드라도 함수로 반복하니 python 시간초과가 안남. 함수로 빼기 전 코드는 pypy로만 통과됨 

for p_v_position in combinations(v_position,M):
    bfs(p_v_position)
    
print(min(answer) if answer else -1)