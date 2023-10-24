'''
3980번 선발명단 골드5

insight
    >> 백트래킹 정석의 문제 
       선수들 한명한명 백트래킹하며 포지션에 능력치를 채움
       포지션 리스트를 모두 채운뒤 합을 비교 --> 최댓값만 저장

문제
https://www.acmicpc.net/problem/3980

예제 입력 1 
1
100 0 0 0 0 0 0 0 0 0 0
0 80 70 70 60 0 0 0 0 0 0
0 40 90 90 40 0 0 0 0 0 0
0 40 85 85 33 0 0 0 0 0 0
0 70 60 60 85 0 0 0 0 0 0
0 0 0 0 0 95 70 60 60 0 0
0 45 0 0 0 80 90 50 70 0 0
0 0 0 0 0 40 90 90 40 70 0
0 0 0 0 0 0 50 70 85 50 0
0 0 0 0 0 0 66 60 0 80 80
0 0 0 0 0 0 50 50 0 90 88
예제 출력 1 
970

'''
import sys
input=sys.stdin.readline

def dfs(position,pos):
    global ans
    
    if len(position)==11:
        ans=max(sum(position),ans)
        return
    
    for i in range(0,11):
        if not visited[i] and athlete[i][pos]:
            visited[i]=True
            position.append(athlete[i][pos])
            dfs(position,pos+1)
            visited[i]=False
            position.pop()

# 테스트 케이스
T= int(input())

for _ in range(T):
    # 11명 운동선수 능력치
    athlete =[list(map(int,input().split())) for _ in range(11)]
    visited=[False]*11
    ans=0
    
    dfs([],0)
    print(ans)
