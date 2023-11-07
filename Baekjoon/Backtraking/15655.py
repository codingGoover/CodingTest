'''
15655번 N과 M(6) 실버3

insight
    >> 저번문제에서 풀어보고 숫지,방문 리스트 두개로 나누었더니
       인덱스 범위가 너무 헷갈렸었음. 생각하기 쉬운대로 하는게 나을까?
       빠른게 나을까. .
       
문제
https://www.acmicpc.net/problem/15655

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 5 2
예제 출력 1 
2
4
5

예제 입력 2 
4 2
9 8 7 1
예제 출력 2 
1 7
1 8
1 9
7 8
7 9
8 9

예제 입력 3 
4 4
1231 1232 1233 1234
예제 출력 3 
1231 1232 1233 1234

'''

import sys
input=sys.stdin.readline

def dfs(len,index):
    if len==M:
        print(*sequence)
        return
    
    for i in range(index+1,N):
        
        if not visited[i]:
            sequence.append(number[i])
            visited[i]=True
            dfs(len+1,i)
            visited[i]=False
            sequence.pop()
            
            
# 자연수개수 N, 수열길이M
N,M= map(int,input().split())
number=sorted(map(int,input().split()))
visited=[False]*(N)
sequence=[]

for i in range(0,N-M+1):
    sequence.append(number[i])
    visited[i]=True
    dfs(1,i)
    visited[i]=False
    sequence.pop()