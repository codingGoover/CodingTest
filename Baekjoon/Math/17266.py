'''
17266번 실버4 어두운 굴다리

insight
>> 그리디인줄 알았는데 수학같음

1 ≤ N ≤ 100,000
'''
import sys
import math
input=sys.stdin.readline

N= int(input())
M= int(input())
X= list(map(int,input().split()))



l=X[0]-0
r=N-X[-1]

ans=max(l,r)
#print(X[:-1])

if len(X)>=2:
    for idx,h in enumerate(X[:-1]):
        if math.ceil((X[idx+1]-h)/2)>ans:
            ans=math.ceil((X[idx+1]-h)/2)
        
print(ans)