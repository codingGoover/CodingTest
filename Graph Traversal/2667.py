'''
2667번 단지번호붙이기 실버1

문제
https://www.acmicpc.net/problem/2667

insight
    >> 그냥 BFS 문제
       하나에 연결된 지점을 파악하기 
       방문되지 않은 시작점을 함수로 호출하기
입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
'''
import sys
from collections import deque

def bfs(startX,startY):
    cnt=1
    queue=deque([(startX,startY)])
    graph[startY][startX]=-1
    
    while queue:
        x,y= queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and graph[ny][nx]==1:
                cnt+=1
                graph[ny][nx]=-1 #방문표시
                queue.append((nx,ny))
    
    block.append(cnt)    
                
    
dx,dy=[-1,1,0,0],[0,0,1,-1]
N= int(input())
graph=[list(map(int,input())) for _ in range(N)]
block=[]

for i in range(N):
    for j in range(N):
        if graph[j][i]==1:
            bfs(i,j)

block.sort()
print(len(block))
print(*block,sep='\n')



