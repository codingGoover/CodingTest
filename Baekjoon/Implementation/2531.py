'''
2531번 회전초밥 실버1

itertools로 deque 슬라이싱하는 방법
https://yongjoonseo.dev/computer%20science/algorithm%20concepts/swea-intermediate21/

다음에 슬라이딩윈도우로 15961번 골드 문제는 rotate방식으로 시간초과남

입력
첫 번째 줄에는 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가 각각 하나의 빈 칸을 사이에 두고 주어진다. 단, 2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d이다. 두 번째 줄부터 N개의 줄에는 벨트의 한 위치부터 시작하여 회전 방향을 따라갈 때 초밥의 종류를 나타내는 1 이상 d 이하의 정수가 각 줄마다 하나씩 주어진다.

출력
주어진 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값을 하나의 정수로 출력한다.

예제 입력 1 
8 30 4 30
7
9
7
30
2
7
9
25
예제 출력 1 
5

예제 입력 2 
8 50 4 7
2
7
9
25
7
9
7
30
예제 출력 2 
4

'''

from collections import deque
import itertools
import sys
input=sys.stdin.readline

# 접시수N, 초밥가짓수d, 연속개수k, 추가초밥번호c
N,d,k,c= map(int,input().split())
max=0
#print(N,d,k,c)
sushi= deque([int(input()) for _ in range(N)])

for i in range(N):
    #print('s',sushi)
    part=set(list(itertools.islice(sushi,k)))
    #print('p',part)
    cnt=len(part)
    if c not in part:
        cnt+=1
    if max<cnt:
        max=cnt
    #print(max,cnt)
    sushi.rotate(1)
    
print(max)

    
    
