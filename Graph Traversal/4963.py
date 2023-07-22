'''
4963번 섬의 개수 실버2

문제
https://www.acmicpc.net/problem/4963

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9

insight
>> input과 동시에 리스트에 입력하는 방법 처음 응용  line92
   대각선 이동 방향 dx,dy 리스트 사용
   visted 리스트를 따로 두지 않고 graph에 값 변경(-1) 활용  

'''

import sys
from collections import deque
input=sys.stdin.readline

#graph: land=1 , sea=0 , visted=-1
def bfs(x,y):
    graph[y][x]=-1
    queue=deque([])
    queue.append((x,y))
    
    while queue:
        newX,newY= queue.popleft()
        
        for i in range (8):
            nx=newX+dx[i]
            ny=newY+dy[i]
            
            if 0<=nx<w and 0<=ny<h:
                if graph[ny][nx]>0:
                    graph[ny][nx]=-1
                    queue.append((nx,ny))
    return 1


#   ↑ ↓ ← → ↗ ↖ ↙ ↘
dx=[0,0,-1,1,1,-1,-1,1] 
dy=[1,-1,0,0,1,1,-1,-1]


while True: 
    w,h= map(int,input().split()) #넓이,높이

    if w+h==0:
        break

    graph=[list(map(int, input().split())) for _ in range(h)]
    #print(*graph, sep='\n')
    island=0

    for y in range(h):
        for x in range(w):
            if graph[y][x]==1:
                island+=bfs(x,y)

    print(island)
 