'''
17266번 실버4 어두운 굴다리

insight
>> 그리디인줄 알았는데 수학같음(84ms) >> 아니다 이분탐색이라함(180ms)
   
1 ≤ N ≤ 100,000

예제 입력1
5
2
1 5
예제 출력1
2

예제 입력2
5
3
1 3 5
예제 출력2
1

'''
import sys
import math
input=sys.stdin.readline

N= int(input())
M= int(input())
X= list(map(int,input().split()))



# 양끝에 적어도 닿아야하는 값(=최소값)
l=X[0]-0
r=N-X[-1]

ans=max(l,r)


# 퐁당퐁당 간격 확인
if len(X)>=2:
    for idx,h in enumerate(X[:-1]):
        if math.ceil((X[idx+1]-h)/2)>ans:
            ans=math.ceil((X[idx+1]-h)/2)
        
print(ans)



#이분탐색 버전 코드
def possible(height):
    
    prev=0  #이전 가로등이 비춘 마지막 지점
    
    for i in range(M):
        if X[i]-height<=prev:
            prev=X[i]+height
        else:
            return False

    return N<=prev

left=1
right=N
result=0

while(left<=right):
    mid=(left+right)//2
    
    if possible(mid):
        right=mid-1
        result=mid
    else:
        left=mid+1

print(result)