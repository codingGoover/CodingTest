'''
11723번 집합 실버5

insight
    >> 집합의 요소를 문자열말고 int로 통일해줘야 시간초과안남

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

'''
import sys
input=sys.stdin.readline

N= int(input())
S= set([])

for _ in range(N):
    cmd=list(input().split())
    if len(cmd)>1:
        cmd[1]=int(cmd[1])
    
    if cmd[0]=='add':
        S.add(cmd[1])
    elif cmd[0]=='remove':
        S.discard(cmd[1])
    elif cmd[0]=='toggle':
        if cmd[1] in S:
            S.discard(cmd[1])
        else:
            S.add(cmd[1])
    elif cmd[0]=='all':
        S=set([i for i in range(1,21)])
        #print(S)
    elif cmd[0]=='empty':
        S=set([])
    else:
        #print(cmd, S)
        print(1 if cmd[1] in S else 0)
        
