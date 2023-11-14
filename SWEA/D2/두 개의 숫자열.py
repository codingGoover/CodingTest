"""
1959. 두 개의 숫자열 D2

문제를 잘 읽자
파이썬 swap a,b=b,a  가능함
"""

import sys
sys.stdin= open("../input.txt","r")

def check(long,l,short,s):
    ans=[]

    for i in range(0,l-s+1):
       ans.append(sum([long[i+j]*short[j] for j in range(s)]))

    return max(ans)


T= int(input())
for t in range(1,T+1):
    N,M= map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    if max(N,M)==N:
        ans= check(A,N,B,M)
    else:
        ans= check(B,M,A,N)

    # B열의 길이가 더 짧을 경우, A와 B swab (이렇게 하면 항상 B열이 더 긺)
    # if len(A) > len(B):
    #     B, A = A, B
    #
    print("#%d %d"%(t,ans))






