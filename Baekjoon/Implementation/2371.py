'''
2371번 파일 구별하기 실버3

문제
https://www.acmicpc.net/problem/2371

>> P&C 코딩대회 1번문제
   해시를 사용한 집합과 맵

'''
import sys
from collections import defaultdict
input=sys.stdin.readline

N= int(input())
file=[list(map(str,input().split()))for _ in range(N)]
maxK=0

for i in file:
    maxK=max(len(i),maxK)
    i.remove('-1')

#print(file)

for k in range(1,maxK):
    d= defaultdict(int)
    for idx,f in enumerate(file):
        key=''.join(f[:k])
        if d[key]==0:
            d[key]=1
            if idx==len(file)-1:
                print(k)
                sys.exit()
        else:
            break
   
