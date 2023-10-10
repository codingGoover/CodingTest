'''
15650번 N과 M(2) 실버3

insight
    >> 백트래킹 정석!
    
문제
https://www.acmicpc.net/problem/15649

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

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
2 3
2 4
3 4

예제 입력 3 
4 4
예제 출력 3 
1 2 3 4

예제 입력 4
5 3
예제 출력 4
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5

'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(len,sequence):
   
    if len==M:
        print(*sequence)
        return
    
    n=sequence[len-1]
    for i in range(n+1,N+1):
        if not visited[i]:
            visited[i]=True
            sequence.append(i)
            
            dfs(len+1,sequence)
            
            #백트래킹
            visited[i]=False
            sequence.pop()
    
# 1부터 N까지 자연수 M개 수열
N,M=map(int,input().split())
visited=[False]*(N+1)

# 오름차순 수열이므로 루트 숫자가 끝까지 갈필요 X   
for i in range(1,N-M+2):
    visited[i]=True
    dfs(1,[i])
    visited[i]=False



