'''
13023번 ABCDE 골드5

insight
    >> DFS + 백트래킹 문제
       백트래킹은 visited 처리를 끝까지 돌고 돌아왔을때 False로 바꿔주어
       다음 턴때도 해당 노드에 다시 접근가능하도록 만들어 주는 것이 포인트이다.

문제
https://www.acmicpc.net/problem/13023

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

예제 입력 1 
5 4
0 1
1 2
2 3
3 4
예제 출력 1 
1

예제 입력 2 
5 5
0 1
1 2
2 3
3 0
1 4
예제 출력 2 
1

예제 입력 3 
6 5
0 1
0 2
0 3
0 4
0 5
예제 출력 3 
0

예제 입력 4 
8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
예제 출력 4 
1

예제 입력 5
6 6
0 1
1 2
1 5
2 3
2 4
2 5
예제 출력 5
1

'''
import sys

def dfs(start,cnt):
    if cnt==4:
        print(1)
        sys.exit()
     
    for x in graph[start]:
         # 현재 노드를 방문처리
        if not visited[x]:
            #print('start:%d  x:%d  cnt:%d'%(v,x,cnt))
            visited[x] =True
            dfs(x,cnt+1)      
            # 백트레킹을 위해 방문처리를 해제 
            visited[x]=False
            #print('**start:%d  x:%d  cnt:%d'%(v,x,cnt))

N,M = map(int,input().split())

graph = [ [] for _ in range(N)]
visited=[False]*(N)

for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)


for i in range(N):
    visited[i]=True
    dfs(i,0)
    visited[i]=False
print(0)
