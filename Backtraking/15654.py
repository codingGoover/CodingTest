'''
15654번 N과 M(5) 실버3

insight
    >> 풀이법 찾아보니 굳이 딕셔너리가 필요 X
       숫자 --> 오름차순대로 리스트에 저장 
       방문 --> 숫자리스트의 순서대로 T/F 저장

문제
https://www.acmicpc.net/problem/15654

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
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8

예제 입력 3 
4 4
1231 1232 1233 1234
예제 출력 3 
1231 1232 1233 1234
1231 1232 1234 1233
1231 1233 1232 1234
1231 1233 1234 1232
1231 1234 1232 1233
1231 1234 1233 1232
1232 1231 1233 1234
1232 1231 1234 1233
1232 1233 1231 1234
1232 1233 1234 1231
1232 1234 1231 1233
1232 1234 1233 1231
1233 1231 1232 1234
1233 1231 1234 1232
1233 1232 1231 1234
1233 1232 1234 1231
1233 1234 1231 1232
1233 1234 1232 1231
1234 1231 1232 1233
1234 1231 1233 1232
1234 1232 1231 1233
1234 1232 1233 1231
1234 1233 1231 1232
1234 1233 1232 1231

'''

import sys
input=sys.stdin.readline


def dfs(len,sequence):
    if len==M:
        print(*sequence)
        return
    
    for n in visited:
        if not visited[n]:
           visited[n]=True
           sequence.append(n)
           dfs(len+1,sequence)
           visited[n]=False
           sequence.pop()

# 자연수 개수 N, 수열 길이 M
N,M= map(int,input().split())

# 입력된 값을 오름차순으로 key,  value=False 인 딕셔너리 생성
visited={num:False for num in sorted(map(int,input().split()))}

for i in visited:
    visited[i]=True
    dfs(1,[i])
    visited[i]=False

