"""
6485. 삼성시의 버스 노선 D3

"""
import sys
sys.stdin=open("../input.txt","r")
T= int(input())
for t in range(1,T+1):
    N= int(input())
    road=[0]*5001
    for _ in range(N):
        a,b=map(int,input().split())
        for i in range(a,b+1):
            road[i]+=1

    P = int(input())
    print(f'#{t}',end=' ')
    for _ in range(P):
        c= int(input())
        print(road[c],end=' ')
    print()
