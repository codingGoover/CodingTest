'''
15649번 N과 M(1) 실버3

insight
    >> 백트래킹 정석 문제!

문제
https://www.acmicpc.net/problem/15649

예제 입력 1 
3 1
예제 출력 1 
1
2
3

예제 입력 2 
4 2
예제 출력 2 
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3

예제 입력 3 
4 4
예제 출력 3 
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1

'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(len,sequence):
 
    if len==M:
        print(*sequence)
        return
    
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            sequence.append(i)
            dfs(len+1,sequence)
            visited[i]=False
            sequence.pop()

#1부터 N까지 자연수 M개
N,M=map(int,input().split())
visited=[False]*(N+1)

for i in range(1,N+1):
    visited[i]=True
    dfs(1,[i])
    visited[i]=False
    
    
'''
visited 필요없이 sequence 안에서 체크하는 방식
시간 - 20ms ↑ 
그치만 코드가 조금 더 깔끔하다
N 범위가 작아서 시간 초과 X

import sys
input = sys.stdin.readline


def dfs():
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(1,N+1):
        if i not in sequence:
            sequence.append(i)
            dfs()
            sequence.pop()

N,M = map(int, input().split())

sequence = []
for i in range(1,N+1):
    sequence.append(i)
    dfs()
    sequence.pop()
'''
    

