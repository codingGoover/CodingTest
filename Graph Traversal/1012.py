'''
1012번 유기농 배추 실버2

문제
https://www.acmicpc.net/problem/1012

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1 
5
1

예제 입력 2 
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
예제 출력 2 
2

예제 입력 3 
1
3 3 6
0 0
1 1
2 2
0 2
2 0
1 2
예제 출력 3 
3

예제 입력 4
1
11 6 60
0 0
1 1
2 1
3 1
4 1
5 1
6 1
7 1
8 1
9 1
10 1
1 2
2 2
3 2
4 2
5 2
6 2
7 2
8 2
9 2
10 2
1 3
2 3
3 3
4 3
5 3
6 3
7 3
8 3
9 3
10 3
1 4
2 4
3 4
4 4
5 4
6 4
7 4
8 4
9 4
10 4
1 5
2 5
3 5
4 5
5 5
6 5
7 5
8 5
9 5
10 5
2 0
3 0
4 0
5 0
6 0
7 0
8 0
9 0
10 0
예제 출력 4
2



'''


import sys
from collections import deque
input=sys.stdin.readline

def bfs(graph,visted,node):
    queue=deque()
    queue.append(visted[node][0])
    visted[node][1]=True
    
    while queue:
        (x,y)= queue.popleft()
        for i in range (4):
            nx=x+dx[i]
            ny=y+dy[i]
            #이동후 좌표가 (M,N)범위 안에 있을 때
            if 0<=nx<M and 0<=ny<N:
                node= graph[ny][nx]
                #노드가 맞으며 해당 노드를 방문하지 않았을 때
                if node!=-1 and visted[node][1]==False:
                    visted[node][1]=True
                    queue.append(visted[node][0])
        
        
            
T= int(input())
#상하좌우 움직임 좌표
dx=[0,0,1,-1]  
dy=[-1,1,0,0]

for _ in range(T):
    M,N,K= map(int, input().split())
    graph=[[-1 for _ in range(M)]for _ in range(N)]
    visted=[]
    cnt=0

    #graph에는 해당xy위치에 노드번호(등장순서)값을 입력
    #visted[0] == 노드 정보 (x,y)
    #visted[1] == 해당노드 방문유무 True/False
    for i in range(K):
        x,y= map(int,input().split())
        graph[y][x]=i
        visted.append([(x,y),False])
    
    #방문 안한 곳으로 바로 접근 -> bfs 탐색
    for i in range(K):
        if visted[i][1]==False:
            bfs(graph,visted,i)
            cnt+=1
    print(cnt)    
    
#print(*visted, sep='\n')