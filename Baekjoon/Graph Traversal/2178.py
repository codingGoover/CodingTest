'''
2178번 미로탐색 실버1

문제
https://www.acmicpc.net/problem/2178

insight
    >> readline -> 맨끝에 붙은 '\n'도 같이 받아온다
       그냥 input() == readline().rstrip()
       정답출력할때 변수 조심 ㅜ

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

예제 입력 1 
4 6
101111
101010
101011
111011
예제 출력 1 
15

예제 입력 2 
4 6
110110
110110
111111
111101
예제 출력 2 
9

예제 입력 3 
2 25
1011101110111011101110111
1110111011101110111011101
예제 출력 3 
38

예제 입력 4 
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
예제 출력 4 
13

예제 입력 5
5 6
111111
100001
101111
101000
111111
예제 출력 5 
10

예제 입력 6
9 9
111110111
111011101
111100001
101110001
110111001
010011101
110001111
100000111
111111111
예제 출력 6 
17

예제 입력 7
6 6
111111
100001
101101
100101
100101
111101
예제 출력 7
11
'''
import sys
from collections import deque
N,M= map(int,input().split())

#띄어쓰기 없이 정수 여러개 입력받아 2차원 배열로 저장하기
maze=[list(map(int,input())) for _ in range(N)]
visted=[[1 for _ in range(M)]for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

queue= deque([(0,0)])

while queue:
    x,y= queue.popleft()
    
    if x+1==M and y+1==N:
        print(visted[y][x])
        sys.exit()
    
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        #print('%d %d' %(nx, ny))
        if 0<=nx<M and 0<=ny<N and maze[ny][nx]==1 and visted[ny][nx]==1:
            visted[ny][nx]= visted[y][x]+1
            queue.append((nx,ny))

#print(*visted, sep='\n')
