'''
10971번 외판원 순회 2 실버2

insight
    >> 나도 외판원 문제 풀어봤다 백트래킹
       min값 처리 방법으로 시간차이 o  

문제
https://www.acmicpc.net/problem/10971

입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.

예제 입력 1 
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
예제 출력 1 
35

'''
import sys
input=sys.stdin.readline

def dfs(cnt,start,cost):
    
    global min
    
    if min!=0 and min<cost:
        return

    # 마지막 돌아올 때
    if cnt==N-1:
        if W[start][end]>0:     
            if min==0 or min> cost+W[start][end] :
                min=cost+W[start][end]      
            return

    for to in range(N):
        if not visited[to] and W[start][to]>0:
            visited[to]=True
            dfs(cnt+1,to,cost+W[start][to])
            visited[to]=False
            
# 도시 수 N
N= int(input())
W=[list(map(int,input().split())) for _ in range(N)]
min=0

for i in range(N):
    visited=[True if j==i else False for j in range(N)]
    end=i
    dfs(0,i,0)

print(min)
    
