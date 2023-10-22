'''
14712번 넴모넴모(Easy) 골드5

insight
    >> 백트래킹을 알아도 조건을 생각해내지 못했을 문제
       그래프판을 백트래킹하면서 넴모(2X2)가 생기지 않도록 채우고 cnt를 새는 방식
       네모를 넣는 경우는 좌측, 상단, 좌상단 중 하나라도 넴모가 없어야 2X2 넴모 사각형이 생기지 않으므로 이를 체크
       
문제
https://www.acmicpc.net/problem/14712


https://kjhoon0330.tistory.com/entry/BOJ-14712-%EB%84%B4%EB%AA%A8%EB%84%B4%EB%AA%A8-Python
'''
import sys
input=sys.stdin.readline

n,m = map(int,input().split())
graph=[[0]*(m+1) for _ in range(n+1)]
cnt=0

def dfs(x,y):
    global cnt
    
    # 종료 조건
    if (x,y)==(1,n+1):
        cnt+=1
        return 
    
    if x==m:
        # 한줄 밑으로 내린다
        nx,ny=1,y+1
    else:
        # 오른쪽으로 한칸 넘긴다
        nx,ny=x+1,y
          
    # x,y에 네모를 넣지 않은 경우 (그대로 0 유지)
    dfs(nx,ny)
    
    # x,y에 네모를 넣을 수 있고 놓는 경우
    if graph[y-1][x]==0 or graph[y-1][x-1]==0 or graph[y][x-1]==0:
        graph[y][x]=1
        dfs(nx,ny)
        graph[y][x]=0
        

dfs(1,1)
print(cnt)