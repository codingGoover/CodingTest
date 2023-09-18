'''
20438번 출석체크 실버2

문제
https://www.acmicpc.net/problem/20438

insight
    >> 졸린지 안졸린지 , 출석한지 안출석 한지 학생의 유무를 
       리스트에 해당 학생 인덱스에 0 또는 1 값으로 표시할 수 있지만 
       생각이 나지 않아 리스트에 있는지 없는지 탐색 한다 생각하여 딕셔너리로 구현했음
       
       나중에 찾아보니 리스트로 조금더 간단하게 구현가능
       메모리 0.5 KB ↓ , 시간 4ms ↓ 
       
       파이썬은 숫자 0 = False 그 외 True
       숫자 개수 = 시작-끝 +1 
       
입력
1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)

2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과 Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.

4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)

출력
M개의 줄에 걸쳐서 각 구간에 대해서 출석이 되지 않은 학생들의 수를 출력하라.

예제 입력 1 
10 1 3 1
7
3 5 7
3 12
예제 출력 1 
4
입장 번호 3번부터 12번까지의 구간에서 입장 번호 4, 8, 11번이 출석 코드를 받지 못했고, 7번은 출석 코드를 받았으나 조느라 출석하지 못했다.

예제 입력 2 
50 4 5 1
24 15 27 43
3 4 6 20 25
3 52
예제 출력 2 
25

예제 입력 3 
50 4 5 2
24 15 27 43
3 4 6 20 25
3 25
26 52
예제 출력 3 
12
13

예제 입력 4
5 1 1 1
3
3
3 7

예제 출력 4 
5

'''

import sys
input=sys.stdin.readline

# 학생수N, 졸고있는학생K, 출석코드보낼학생Q, 주어진구간M
N,K,Q,M= map(int,input().split())

#딕셔너리 활용
studentQ=dict()
studentK=dict()
psum=[0]*(N+3)

for k in map(int,input().split()):
    studentK[k]=1

for q in map(int,input().split()):
    if q in studentK:
        continue
    for i in range(q,N+3,q):
        if i not in studentK:
            studentQ[i]=0

for i in range(3,N+3):
    if i in studentQ:
        psum[i]=psum[i-1]
    else:
        # 출석하지 않은 학생을 카운트 
        psum[i]=psum[i-1]+1

rangeQ=[tuple(map(int,input().split())) for _ in range(M)]

for x1,x2 in rangeQ:
    ssum=psum[x2]-psum[x1-1]
    print(ssum)


#-----------------------------------------------------------------#
# 리스트로 변경하면

import sys
input=sys.stdin.readline
N,K,Q,M= map(int,input().split())


sleep=[0]*(N+3)
attend=[0]*(N+3)
psum=[0]*(N+3)

for i in map(int,input().split()):
    sleep[i]=1
    
for i in map(int,input().split()):
    if sleep[i]:
        continue
    for j in range(i,N+3,i):
        if not sleep[j]:
            attend[j]=1

for i in range(3,N+3):
    psum[i]=psum[i-1]+attend[i]

for _ in range(M):
    x1,x2= map(int,input().split())
    ans= x2-x1+1 - (psum[x2]-psum[x1-1])
    print(ans)