'''
11123번 양한마리두마리 실버2

문제
https://www.acmicpc.net/problem/11123

insight
    >> BFS탐색 횟수 문제 
       nx, ny 변수 순서 조심

입력
첫 번째 줄은 테스트 케이스의 수를 나타나는 T를 입력받는다.

이후 각 테스트 케이스의 첫 번째 줄에서는 H,W 를 입력받는다. H는 그리드의 높이이고, W는 그리드의 너비이다. 이후 그리드의 높이 H 에 걸쳐서 W개의 문자로 이루어진 문자열 하나를 입력받는다. 

0 < T ≤ 100
0 < H, W ≤ 100

출력
각 테스트 케이스마다, 양의 몇 개의 무리로 이루어져 있었는지를 한 줄에 출력하면 된다. 

예제 입력 1 
2
4 4
#.#.
.#.#
#.##
.#.#
3 5
###.#
..#..
#.###
예제 출력 1 
6
3

'''

from collections import deque

def bfs(startX,startY):
    queue=deque([(startX,startY)])
    graph[startY][startX]='.'
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<W and 0<=ny<H and graph[ny][nx]=='#':
                graph[ny][nx]='.'
                queue.append((nx,ny))
    return 1


T= int(input())
dx,dy=[-1,1,0,0],[0,0,-1,1]
cnt=[0]*T

for t in range(T):
    H,W= map(int,input().split())
    graph=[list(input()) for _ in range(H)]
   
    for i in range(H):
        for j in range(W):
            if graph[i][j]=='#':
                cnt[t]+= bfs(j,i)
    
print(*cnt,sep='\n')