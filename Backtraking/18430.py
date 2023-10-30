'''
18430번 무기공학 골드4

insight
    >> 백트래킹
       좌표범위 체크, return 조건 등 처음 생각한 방식대로 밀고나가봐야함
       백트래킹 논리보다 x,y 좌표 인덱스 체크에서 삽질 오랫동안한 문제이다
       계속 x와y는 진행이 되어야하고 끝에 도달했을때 리턴, 이 조건값을 잘 따져야한다. 
       조건문 거는 타이밍이나,, 값을 바꾸고 체크할지 값을 바꾸기 이전에 체크할지 

문제
https://www.acmicpc.net/problem/18430      


입력
첫째 줄에는 길동이가 가지고 있는 나무 재료의 세로, 가로 크기를 의미하는 두 자연수 N, M이 주어진다. (1 ≤ N, M ≤ 5) 다음 N개의 줄에 걸쳐서, 매 줄마다 나무 재료의 각 위치의 강도를 나타내는 M개의 자연수 K가 공백을 기준으로 구분되어 주어진다. (1 ≤ K ≤ 100)

출력
첫째 줄에 길동이가 만들 수 있는 부메랑들의 강도 합의 최댓값을 출력한다.

단, 나무 재료의 크기가 작아서 부메랑을 하나도 만들 수 없는 경우는 0을 출력한다.

예제 입력 1 
3 3
32 83 75
24 96 56
71 88 12
예제 출력 1 
632

예제 입력 2 
1 1
7
예제 출력 2 
0

예제 입력 3
2 5
100 1 1 1 1
1 1 100 1 100 
예제 출력 3
606

'''

import sys
input=sys.stdin.readline

def dfs(x,y):
    global ans
    
    # 나무 재료 끝 도달
    if (x,y) == (M-1,N-1):
        ans=max(sum(strength),ans)
        return
         
    if x==M-1:
        x, y = 0, y+1
        #print('--')
    else:
        x+=1
         
    #print('xxx:%d yyy:%d'%(x,y))
   
    if not visited[y][x]:
     
        for i in range(4):
            nx1,nx2=dx[i][0]+x,dx[i][1]+x
            ny1,ny2=dy[i][0]+y,dy[i][1]+y
                    
            if 0<=nx1<M and 0<=nx2<M and 0<=ny1<N and 0<=ny2<N:
                if not (visited[ny1][nx1] or visited[ny2][nx2]):
                  
                    visited[y][x]=visited[ny1][nx1]=visited[ny2][nx2]=True
                    #print()
                    #print('xx:%d yy:%d'%(x,y))
                    #print(*visited,sep='\n')
                    strength.append(material[y][x]*2 + material[ny1][nx1]+ material[ny2][nx2])
                  
                    dfs(x,y)
                    
                    strength.pop()
                    visited[y][x]=visited[ny1][nx1]=visited[ny2][nx2]=False
                    #print()
                    #print('back')
                    #print('x:%d y:%d'%(x,y))
                    #print(*visited,sep='\n')

    dfs(x,y)
        

# 세로N, 가로M
N,M= map(int,input().split())
material=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]
strength=[]
ans=0
dx=[(-1,0),(-1,0),(0,1),(0,1)]
dy=[(0,1),(0,-1),(-1,0),(1,0)]

dfs(-1,0)
print(ans)
