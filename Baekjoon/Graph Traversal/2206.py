'''
2206번 벽 부수고 이동하기 골드3

>> 전형적인 다른 이동방법이 있는 문제. 말이 되고 싶은 원숭이/ 프로그래머스 보물상자
   헤매지 않고. visit 배열을 3차원으로(벽을 부셨을때/아닐때) 등 제한되어있는 변수를 3차원으로
   그리고 안부셨을 경우 부실수 있으므로 부셨을 때 visit 값을 변경해주고 방문한곳인지 아닌지 봐야함
   
입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15

예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1

'''

from collections import deque
import sys
input=sys.stdin.readline
#세로 N 가로 M
N,M=map(int,input().split())
MAP=[]
# 벽o/x  Y  X
visit=[[[-1]*M for _ in range(N)]for _ in range(2)]
visit[0][0][0]=1
visit[1][0][0]=1

for _ in range(N):
    MAP.append(input().rstrip())
#print(MAP)
dx,dy=[0,0,-1,1],[-1,1,0,0]
# (x,y,w)
queue= deque([(0,0,0)])

while queue:
    x,y,w= queue.popleft()
    if (x,y)==(M-1,N-1):
        print(visit[w][y][x])
        sys.exit()

    # 하나의 반복문에 벽부수는 경우/ 그냥 이동하는 경우 같이 하니 1초 정도 더빨라짐
    for i in range(4):
        nx,ny= x+dx[i], y+dy[i]
        if 0>nx or nx>=M or 0>ny or ny>=N:
            continue
        if MAP[ny][nx]!='1' and visit[w][ny][nx]==-1:
            visit[w][ny][nx]= visit[w][y][x]+1
            queue.append((nx,ny,w))
        if w==1:
            continue
        if MAP[ny][nx]=='1' and visit[w+1][ny][nx]==-1:
            visit[w + 1][ny][nx] = visit[w][y][x] + 1
            queue.append((nx, ny, 1))

    # # 벽 부수기
    # for i in range(4):
    #     nx, ny = x + dx[i], y + dy[i]
    #     if 0 <= nx < M and 0 <= ny < N and MAP[ny][nx]=='1' and visit[w+1][ny][nx]==-1:
    #         visit[w+1][ny][nx] = visit[w][y][x] + 1
    #         queue.append((nx, ny, w+1))


print(-1)

