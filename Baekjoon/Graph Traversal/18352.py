'''
18352번 특정 거리의 도시찾기 실버2

insight
    >> bfs 와 dfs 중에 고민했는데 dfs일까 싶었다만, 알고리즘에 너비우선탐색이라하여 그렇게 풀었음.
       뭐가 더 적당한지 생각을 잘 해야겠음 

문제
https://www.acmicpc.net/problem/18352

입력
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

출력
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

예제 입력 1 
4 4 2 1
1 2
1 3
2 3
2 4
예제 출력 1 
4

예제 입력 2 
4 3 2 1
1 2
1 3
1 4
예제 출력 2 
-1

예제 입력 3 
4 4 1 1
1 2
1 3
2 3
2 4
예제 출력 3 
2
3

'''

import sys
from collections import deque
input=sys.stdin.readline
#도시개수 N, 도로개수 M, 거리정보 K, 출발도시 X
N,M,K,X = map(int,input().split())

path=[[]for _ in range(N+1)]
visit=[True if i==X else False for i in range(N+1)]
ans=[]

for _ in range(M):
    c1,c2=map(int,input().split())
    path[c1].append(c2)
    
queue=deque([(X,0)])

while queue:
    city,depth= queue.popleft()
    
    if depth==K:
        ans.append(city)
        continue
        
    for c in path[city]:
        if not visit[c]:
            visit[c]=True
            queue.append((c,depth+1))

if not ans:
    print(-1)
else:
    ans.sort()
    print(*ans,sep='\n')