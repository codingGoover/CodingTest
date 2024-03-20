'''
15961번 회전초밥 골드4

insight
>> 슬라이딩 윈도우
    빠른 중복처리는 set보다 딕셔너리가 훨씬 유리하다!
    디폴트딕셔너리에 key: 등장개수value 
    value가 0이되면 삭제
    len(딕셔너리) 로 개수 체크 
       
문제
https://www.acmicpc.net/problem/15961

'''

from collections import defaultdict
import sys
input=sys.stdin.readline

# 접시수N, 초밥가짓수d, 연속개수k, 추가초밥번호c
N,d,k,c= map(int,input().split())


sushi=[int(input()) for _ in range(N)]
window=defaultdict(int)

for i in range(k):
    window[sushi[i]]+=1

window[c]+=1
ans=len(window)


for i in range(N):
    window[sushi[i]]-=1
    if window[sushi[i]]==0:
        del window[sushi[i]]
    window[sushi[(i+k)%N]]+=1
    ans=max(len(window),ans)
    
print(ans)
