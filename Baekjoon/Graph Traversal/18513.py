'''
18513번 샘터 골드4

문제
https://www.acmicpc.net/problem/18513

insight
    >> 무!조!건! 딕셔너리!! 문제 
       샘터의 위치가 -1억 ~ 1억 범위가 엄청 크다
       딕셔너리로 풀라고 만든 문제
       home (=visted) 에 해당 위치가 있는지 포함여부 확인
       리스트  vs  딕셔너리
       하나하나 선형탐색 --> 키 확인으로 바로 접근
       a[key]	O(1)	키를 조회하여 값을 리턴한다. 
       List : 삽입, 제거, 탐색, 포함여부확인 모두 O(n)
       Set과 Dictionary : 삽입, 제거, 탐색, 포함여부확인 연산 O(1)
       
    >> 숨바꼭질과 비슷한 일차원 BFS문제
    

입력
첫째 줄에 자연수 N과 K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N, K ≤ 100,000) 둘째 줄에 N개의 샘터의 위치가 공백을 기준으로 구분되어 정수 형태로 주어진다. (-100,000,000 ≤ 샘터의 위치 ≤ 100,000,000) 단, 모든 N개의 샘터의 위치들은 서로 다르게 주어진다.

출력
첫째 줄에 모든 집에 대한 불행도의 합의 최솟값을 출력한다.

예제 입력 1 
2 5
0 3
예제 출력 1 
6

예제 입력 2 
2 100000
-100000000 100000000
예제 출력 2 
1250050000

'''
import sys
from collections import deque
input = sys.stdin.readline

# N샘터 K집 개수
N,K= map(int,input().split())
water= list(map(int,input().split()))

# 키 검색을 위한 딕셔너리 사용 
# key= 위치 , value= 불행도 
home=dict()
queue=deque([])
sum=0

for w in water:
    home[w]=0       # [key] = value
    queue.append(w)

while queue:
    x= queue.popleft()
    for nx in [x-1,x+1]:
        
        if nx not in home: 
            queue.append(nx)
            home[nx]=home[x]+1
            sum+=home[nx]
     
            if len(home)-len(water)==K:
                print(sum)
                sys.exit()
        
        
            
        

