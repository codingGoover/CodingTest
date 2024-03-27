'''
2164번 가드2 실버4

insight
>> 그냥 구현아닐까? 했는데 그냥 데큐 문제임

시간제한 2초

입력범위
1 ≤ N ≤ 500,000

'''

import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
queue=deque([i for i in range(1,N+1)])

# 빼고 넣고를 한번의 행동으로 봐도 됨..
# 문제대로 뺀다, 끝에 넣는다 숫자따라서 다르게 할필요가 없음 (380ms -> 252ms)
while len(queue)>1:
    
    queue.popleft()
    queue.append(queue.popleft())  

print(queue[0])
