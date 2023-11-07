'''
1174번 줄어드는 수 골드5

insight
    >> 백트래킹
       복잡하게 생각할게 아니라 단순하게 줄어두는 수를 먼저 구해놓고
       정답을 출력하는 문제,, 백트래킹 순서도 숫자 순대로 나와야 하나 꼬아서 생각해서 어려웠음
    
문제
https://www.acmicpc.net/problem/1174

'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(num):
    
    strr= ''.join(map(str,num))
    decrease.append(int(strr))
    
    for i in range(0,num[-1]):        
        num.append(i)
        dfs(num)
        num.pop()
        

N= int(input())
decrease=[]

for i in range(0,10):
    dfs([i])
    
decrease.sort()
if N >len(decrease):
    print(-1)
else:    
    print(decrease[N-1])


# 1038번 출력
# decrease.sort()
# if N >=len(decrease):
#     print(-1)
# else:    
#     print(decrease[N])



