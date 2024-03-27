'''
13305번 실버3 주유소

insight
>> 그리디 알고리즘

서브테스트 58점
2 ≤ N ≤ 1,000 넘어가니까 시간초과 
그래서 heapq 로 정렬을 대신했는데 여전히 58점
누적합도 넣어봤지만 이게아닌가봄

진짜 삽질대마왕
그냥 그리디,,

시간제한 2초
2 ≤ N ≤ 100,000

'''
import heapq
import sys
input=sys.stdin.readline

N=int(input())
load=list(map(int,input().split()))
cost=list(map(int,input().split()))
cost.pop() #어짜피 맨끝에꺼 필요X
cost=dict(zip([i for i in range(N-1)],cost))

psum=[0]*N
for i in range(1,N):
    psum[i]=psum[i-1]+load[i-1]

sum=0

prev=N-1
while prev!=0:
    
    city=prev
    s=list(zip(cost.values(),cost.keys()))
    #s= sorted(cost.items(),key=lambda x: x[1])
    heapq.heapify(s)
    
    while len(s)>0:
        
        co,lo= heapq.heappop(s)
    
        if lo<=city:
            sum+=(psum[city]-psum[lo])*co
            prev=lo
            break
    
    for i in range(prev,city):
        del cost[i]
        
print(sum)




# 이게 맞냐 그리디,,,하

n=int(input())
roads=list(map(int,input().split()))
costs=list(map(int,input().split()))

res=0
m=costs[0]

for i in range(n-1):
    if costs[i]<m:
        m=costs[i]
    res+=m * roads[i]

print(res)