'''
15651번 N과 M(3) 실버3

insight
    >> 중복체크 없는 백트래킹!
    
문제
https://www.acmicpc.net/problem/15651

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

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
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4

예제 입력 3 
3 3
예제 출력 3 
1 1 1
1 1 2
1 1 3
1 2 1
1 2 2
1 2 3
1 3 1
1 3 2
1 3 3
2 1 1
2 1 2
2 1 3
2 2 1
2 2 2
2 2 3
2 3 1
2 3 2
2 3 3
3 1 1
3 1 2
3 1 3
3 2 1
3 2 2
3 2 3
3 3 1
3 3 2
3 3 3

'''
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(len,sequence):
    if len==M:
        print(*sequence)
        return
    
    for i in range(1,N+1):
        sequence.append(i)
        dfs(len+1,sequence)
        sequence.pop()

# 1부터 N까지 자연수 M개 수열
N,M= map(int,input().split())

for i in range(1,N+1):
    dfs(1,[i])



'''
# 500ms ↓ 더 간단한 코드. 중복체크X기에 DFS() 한번만 호출해도됨
 
n,m= map(int,input().split())
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()

'''