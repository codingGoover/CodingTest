'''
[PCCP 모의고사 #2] 2번 - 신입사원 교육 Lv2

>> 그리디, 힙
   길이 1000000 을 해결할 수 있는 힙 자료구조 
   pop, push -> 시간복잡도: log n

'''

import heapq

def solution(ability, number):
    answer = 0
    heapq.heapify(ability)
    
    for n in range(number):
        s_h=heapq.heappop(ability)+heapq.heappop(ability)
        heapq.heappush(ability,s_h)
        heapq.heappush(ability,s_h)
    
    answer=sum(ability)
        
    return answer