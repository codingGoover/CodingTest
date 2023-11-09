import sys
sys.stdin=open("../input.txt","r")
input= sys.stdin.readline
T= int(input())
DIRS=[[1,0],[0,1],[-1,0],[0,-1]]

for t in range(1,T+1):
    N= int(input())
    snail=[[0]*N for _ in range(N)]
    x,y,n,i=-1,0,0,0

    while i<N*N:
        nx,ny= x+ DIRS[n%4][0], y+DIRS[n%4][1]
        if 0<=nx<N and 0<=ny<N and not snail[ny][nx]:
                x,y=nx,ny
                i+=1
                snail[ny][nx]=i
        else:
            n+=1


    print("#%d"%t)
    #print(*snail,sep='\n')

    for row in snail:
        print(*row)  # 1차원 리스트를 풀면 원소만 출력됨

    #print('\n'.join([' '.join(map(str,row)) for row in snail]))