import sys

input=sys.stdin.readline

N= int(input())
if N%2==0:
    print('CY')
else:
    print('SK')

'''

DP 방식
게임 진행의 턴을 왔다 갔다한 최소 개수를 찾음 
홀수? 상근
짝수? 창영

'''

N= int(input())
DP=[0,1,2]   # 0번 1번(상근) 2번(상근-창영)

for i in range(3,N+1):
    DP.append(min(DP[i-1],DP[i-3])+1)

if DP[N]%2==0:
     print('CY')
else:
    print('SK')

