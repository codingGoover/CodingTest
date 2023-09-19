'''
16973번 직사각형 탈출 골드4

문제
https://www.acmicpc.net/problem/16973

insight
    >> BFS, 이동 불가능한 벽이 사각형 범위에 속하는 지 아닌지 검사 
       적은 경우의 수로 생각해야 시간초과가 안나는 문제
       좌표의 이동 --> 벽에 거리는지 (X)
       벽 좌표     -->  이동후 사각형 범위 안에 있는지 (O)
       
       BFS + 누적합 
       해당 사각형 구간에 벽이 한개라도 존재하는지 
       누적합의 구간합을 구해서 검사할 수도 있음
       
       시간차이 약 2000ms ↓
       이문제로 누적합을 알게되었지만 필수 사용 알고리즘은 아니었음
       
       
입력
첫째 줄에 격자판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 각 칸의 정보가 주어진다. 0은 빈 칸, 1은 벽이다.

마지막 줄에는 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc가 주어진다.

격자판의 좌표는 (r, c) 형태이고, r은 행, c는 열이다. 1 ≤ r ≤ N, 1 ≤ c ≤ M을 만족한다.

출력
첫째 줄에 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

제한
2 ≤ N, M ≤ 1,000
1 ≤ H ≤ N
1 ≤ W ≤ M
1 ≤ Sr ≤ N-H+1
1 ≤ Sc ≤ M-W+1
1 ≤ Fr ≤ N-H+1
1 ≤ Fc ≤ M-W+1
입력으로 주어진 직사각형은 격자판을 벗어나지 않고, 직사각형이 놓여 있는 칸에는 벽이 없다.


예제 입력 1 
4 5
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
2 2 1 1 1 4
예제 출력 1 
7
아래, 아래, 오른쪽, 오른쪽, 오른쪽, 위, 위

예제 입력 2 
6 7
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
0 0 0 0 0 0 0
2 3 1 1 5 5
예제 출력 2 
8


반례
5 5
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
3 3 3 1 3 3
// Answer : 2

5 5
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
3 3 3 1 3 1
// Answer : 0

5 5
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
3 3 3 1 3 4
// Answer : -1
    
5 5
0 1 0 0 0
0 1 0 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
1 1 1 1 3 3
// Answer : 16

8 8
0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0
0 0 1 0 0 1 0 0
0 0 1 0 0 1 0 0
0 0 1 1 1 1 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0
2 2 1 1 3 4
// Answer : 23
    
8 8
0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0
0 0 1 0 0 1 0 0
0 0 1 0 0 1 0 0
0 0 1 1 1 1 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0
2 2 3 4 1 1
// Answer : 23

'''

import sys
from collections import deque
input=sys.stdin.readline

def checkPsum(r,c):
    ssum= psum[r+H-1][c+W-1] - psum[r+H-1][c-1] - psum[r-1][c+W-1] + psum[r-1][c-1]
    if ssum>0:
        return False
    return True
    

def check(r,c):
    for wr, wc in wall:
        if r<=wr<= r+H-1 and c<=wc<=c+W-1:
            return False
    return True

#격자판 높이N 너비M
N,M= map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
wall=[]
dx,dy=[-1,1,0,0],[0,0,-1,1]
psum=[[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        psum[i+1][j+1]= grid[i][j]+psum[i][j+1]+psum[i+1][j]-psum[i][j]
        if grid[i][j]==1:
            wall.append((i,j))

#사각형 높이H, 너비W, 시작점 행열, 끝점 행열            
H,W,Sr,Sc,Fr,Fc= map(int,input().split())

if Sr==Fr and Sc==Fc:
    print(0)
    sys.exit()
    
queue= deque([(Sr-1,Sc-1,0)])
grid[Sr-1][Sc-1]= -1

while queue:
    r,c,time=queue.popleft()
    #print('%d %d'%(r,c))
    
    for i in range(4):
        nr=r+dy[i]
        nc=c+dx[i]
        
        if 0<=nr<N-H+1 and 0<=nc<M-W+1 and grid[nr][nc]==0:
            if check(nr,nc):            # --> 벽 좌표 리스트로 check하는 함수
           #if checkPsum(nr+1,nc+1):      --> 누적합의 구간합으로 check하는 함수
                  
                #print('nr%d nc%d'%(nr,nc))
                if nr==Fr-1 and nc==Fc-1:
                   print(time+1) 
                   sys.exit()
                   
                grid[nr][nc]=-1
                queue.append((nr,nc,time+1))
            
print(-1) 
    

