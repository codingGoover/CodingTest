'''
프로세스 Lv2 
대놓고 큐 문제

정렬된 우선순위 리스트를 따로 두지 않고
큐 안에서 더 큰게 있는지 찾는 방법도 있음

# 어떤것 하나라도 크면 다시 큐삽입
if any(cur[1] < q[1] for q in queue):
    queue.append(cur)

'''
from collections import deque
def solution(priorities, location):
    
    queue=deque([])
    
    for idx,p in enumerate(priorities):
        queue.append((idx,p))
        
    priorities.sort(reverse=True)
    answer = 0
    
    while True:
        
        #print(queue)
        
        idx,p= queue.popleft()
        
        if priorities[0]!=p:
            queue.append((idx,p))
        else: # 최고 우선순위 경우
            priorities.pop(0)
            answer+=1
            if idx==location:
                return answer
