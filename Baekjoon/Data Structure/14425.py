'''
14425번 문자열 집합 실버4

insight
    >> 문제이해를 잘못했었음. 집합에 문자열 포함이 아니라 그냥 같은건지 체크를 해야하는 문제
       포함하는지 알기위해서는 in , find 연산 사용하면 됨  
       
문제
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다. 

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

예제 입력 1 
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

예제 출력 1 
4

'''

import sys
input=sys.stdin.readline

# 집합개수 N , 검사 문자열개수 M
N,M= map(int,input().split())
d= dict()
ans=0

for _ in range(N):
    str = input().rstrip()
    d[str]=True

for _ in range(M):
    str= input().rstrip()
    if d.get(str,False):
        ans+=1
    # else: #안똑같은경우
    #     for k in d.keys():
    #         if str in k:
    #             print(str, k)
    #             ans+=1
    #             break

print(ans)
    
            

    