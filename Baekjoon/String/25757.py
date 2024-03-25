'''
25757번 임스와 함께하는 미니게임 실버5

insight
>>  문자열
    해시를 사용한 집합과 맵

입력범위
1<=N<=100,000

'''
import sys
from collections import defaultdict

input=sys.stdin.readline

N,K= input().split()
game={'Y':1,'F':2,'O':3}
people=defaultdict(bool)
team,ans=0,0

for _ in range(int(N)):
    name=input().rstrip()
    if people[name]==True:
        continue

    people[name]=True
    team+=1
    if team==game[K]:
        team=0
        ans+=1

print(ans)


