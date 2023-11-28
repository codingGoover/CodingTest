'''
[PCCP 모의고사 #2] 3번 - 카페 확장 Lv3

>> 구현, 시뮬레이션, 큐
   큐를 활용해서 시간을 넣었다 뺐다하기
'''

from collections import deque

def solution(menu, order, k):
    answer = 0
    queue=deque([])
    N= len(order)
    in_time=[i for i in range(0,N*k,k)]
    #print(in_time)
    
    time=0
    
    for idx, cur in enumerate(in_time):
        while len(queue)>0:
            if cur>=queue[0][1]:
                queue.popleft()
            else:
                break
                
        if len(queue)>0:
            time=queue[-1][1]
        else:
            time=cur
            
        esti_time =  time + menu[order[idx]]
        queue.append((time,esti_time))
        #print(queue)
        answer=max(answer,len(queue))
        
    
    return answer