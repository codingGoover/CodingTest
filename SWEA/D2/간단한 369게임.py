"""
1926. 간단한 369게임 D2

나는 369 룰도 모르는 바보

"""
import sys
sys.stdin= open("../input.txt","r")

N= int(input())
numbers=[ str(i) for i in range(1,N+1)]

for num in numbers:
    cnt=0
    for n in num:
        if n in ['3','6','9']:
            cnt+=1
    if cnt>0:
        print('-'*cnt,end=' ')
    else:
        print(num,end=' ')
