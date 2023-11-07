'''
15666번 N과 M(12) 실버3

insight
    >> 15665번 유형 + 같은 수 중복가능  
       중복수열 체크는 prev변수
       중복 방문 가능이므로 자기자신 인덱스부터 방문 range(idx,N) 

문제
https://www.acmicpc.net/problem/15666

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4

예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 1
1 7
1 9
7 7
7 9
9 9

예제 입력 3 
4 4
1 1 2 2
예제 출력 3 
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2

'''
import sys
input=sys.stdin.readline

def dfs(len,idx):
    prev=0
    
    if len==M:
        print(' '.join(map(str,sequence)))
        return
    
    for i in range(idx,N):
        if prev!=number[i]:
            
            sequence.append(number[i])
            prev=number[i]
            
            dfs(len+1,i)
            sequence.pop()
        

# N개의 자연수 중 수열길이 M
N,M= map(int,input().split())
number=sorted(map(int,input().split()))

sequence=[]

dfs(0,0)
