"""
1600번 말이 되고픈 원숭이 골드3

반례
1
1 1
0
0

2
10 2
0 0 1 0 0 1 0 0 1 0
0 0 1 1 0 0 0 0 1 0
10

1
5 5
0 1 1 0 1
0 0 1 0 1
0 1 0 1 1
0 1 0 1 0
1 1 0 1 0
-1

2
5 3
0 0 0 0 0
1 0 1 1 0
1 0 1 1 0
4

5
6 6
0 0 0 0 0 1 
0 0 0 1 0 1 
0 1 0 0 0 1 
0 1 0 0 1 0 
0 0 0 0 0 1 
1 0 0 0 1 0
4	

1
4 4
0 0 0 0
0 0 0 0
0 0 1 1
0 0 1 0
4

"""
import sys
from collections import deque
input=sys.stdin.readline

# 말움직임 횟수 K
K= int(input())

# 가로 W 세로 H
W,H= map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(H)]
visited = [[[False for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

queue=deque([(0,0,K,0)])
visited[0][0][0]=True
hdx=[-2,-1,1,2,-2,-1,1,2]
hdy=[1,2,2,1,-1,-2,-2,-1]

mdx=[1,-1,0,0]
mdy=[0,0,1,-1]


while queue:
    x,y,k,l= queue.popleft()
    #print(f'x:{x} y:{y} k:{k} l:{l}')

    if (x,y)==(W-1,H-1):
        print(l)
        sys.exit()

    # 말의 움직임
    if k>0:
        for i in range(8):
            nx,ny=x+hdx[i],y+hdy[i]
            if 0<=nx<W and 0<=ny<H and graph[ny][nx]==0 and not visited[k-1][ny][nx]:
                visited[k-1][ny][nx]=True
                queue.append((nx,ny,k-1,l+1))
                #print("말",nx,ny,k-1,l+1)

    # 원숭이의 움직임
    for i in range(4):
        nx,ny=x+mdx[i],y+mdy[i]
        if 0<=nx<W and 0<=ny<H and graph[ny][nx]==0 and not visited[k][ny][nx]:
            visited[k][ny][nx]=True
            queue.append((nx,ny,k,l+1))
            #print("원숭이",nx,ny,k,l+1)
            
#print(visited)
print(-1)