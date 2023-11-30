'''
14503번 로봇 청소기 골드5

>> 알고리즘이 필요없는 구현문제
   방향설정과 전진/후진을 푼적이 있어서 아이디어는 바로 떠올랐지만,
   구현을 하려하니 조건문에서 생각보다 시간이 걸렸다...
   그리고 2차원배열의 y인덱스의 북쪽은 y-1  남쪽은 y+1 인데 거꾸로 생각해버렸다.
   방향을 잊지 말것
   

입력
첫째 줄에 방의 크기 N과 M이 입력된다. 
(3<= N, M<=50)둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 
(r, c)와 처음에 로봇 청소기가 바라보는 방향 d가 입력된다. 
d가 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽을 바라보고 있는 것이다.

셋째 줄부터 
N개의 줄에 각 장소의 상태를 나타내는 N X M개의 값이 한 줄에 M개씩 입력된다. 
i번째 줄의 j번째 값은 칸 (i, j)의 상태를 나타내며, 이 값이 0인 경우 
(i, j)가 청소되지 않은 빈 칸이고, 1인 경우 
(i, j)에 벽이 있는 것이다. 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 
로봇 청소기가 있는 칸은 항상 빈 칸이다.

출력
로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

예제 입력 1 
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력 1 
1

예제 입력 2 
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
예제 출력 2 
57
   
'''

import sys
input=sys.stdin.readline
# 세로N 가로M
N,M= map(int,input().split())
# 위치 r,c 방향 d
y,x,d= map(int,input().split())
room=[list(map(int,input().split()))for _ in range(N)]
ans=0

# 북 동 남 서  <-- 우리가 생각하는 방향이 아니라 인덱스 기준에서 북쪽이면 y-1 이다. 생각 실수한 부분!
DIR=[(0,-1),(1,0),(0,+1),(-1,0)]

while True:
    
    if room[y][x]==0:
        room[y][x]=2
        ans+=1
        
    
    # print(f'x{x} y{y} DIR{d}')
    # print(*room ,sep='\n')
    
    noclean,clean=0,0
    for i in range(4):
        nx,ny=x+DIR[i][0],y+DIR[i][1]
        if 0<=nx<M and 0<=ny<N:
            if room[ny][nx]!=0:
                clean+=1
            else:
                noclean+=1
                
    if clean==4:
        #print(f'x{x} y{y} clean')
        nx,ny=x-DIR[d][0],y-DIR[d][1]
        if room[ny][nx]==1:
            break
        else:
            x,y=nx,ny
            continue
    
    if noclean>0:
        #print(f'x{x} y{y} noclean')
        for _ in range(4):
            d=(d-1)%4
            nx,ny=x+DIR[d][0],y+DIR[d][1]
            if room[ny][nx]==0:
                x,y=nx,ny
                break

print(ans)
             
    
        
        
            
            
        
    
        
