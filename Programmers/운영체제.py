'''
[PCCP 모의고사 #1] 4번 - 운영체제 Lv3

>> 힙 (heap)  인덱스 오류나면 시간끌지말고 파이썬튜터로 빨리 확인하기,,

'''
import heapq
    
def solution(program):
    answer = [0 for _ in range(11)]
    heap= []
    ready=[]
    time=dict()
    cur=0
    
    for p in program:
        heapq.heappush(heap,(p[1],p[0]))
        time[(p[1],p[0])]=p[2]
   

    while heap or ready:
        
        #지나온 시간이면 레디힙으로 옮겨줌
        while heap and heap[0][0]<=cur:
            c,s=heapq.heappop(heap)
            heapq.heappush(ready,(s,c)) 
        
        # print('hh',heap)
        # print('rr',ready)
        # print(f'cur:{cur}')
            
        if heap and not ready:
            c,s = heapq.heappop(heap)
            cur=c
            heapq.heappush(ready,(s,c))
            
        score,call= heapq.heappop(ready)
        # print('h',heap)
        # print('r',ready)
        
        answer[score] += cur-call
        cur+=time[(call,score)]
        
        # print(f'cur:{cur} call:{call} score:{score}')
    
    answer[0]=cur
 
    return answer

'''
안풀려서 찾아본 다른사람 코드 
'''

import heapq

def solution(program):

    answer = [0] * 11
    heap = []                            # 우선순위 큐

    program.sort(key=lambda x: (x[1], x[0]))    # 호출된 시각과 우선순위를 기준으로 정렬

    time = 0

    while program or heap:
        
        while program and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))

        if program and not heap:
            time = program[0][1]
            heapq.heappush(heap, program.pop(0))

        temp = heapq.heappop(heap)

        answer[temp[0]] += (time - temp[1])
        time += temp[2]

    answer[0] = time
    return answer