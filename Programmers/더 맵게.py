'''
더 맵게 Lv2 

>> 최소값으로 판별되므로 최소힙을 사용하면 시간초과를 면할 수 있다.
   힙 heapq 를 활용하여야함

'''
import heapq

def solution(scoville, K):
    answer = 0
    # 리스트를 최소힙으로 만들어줌
    heapq.heapify(scoville)
    
    # 최소힙: 노드가 가장 최소값
    while len(scoville)>1 and scoville[0]<K:
        m1=heapq.heappop(scoville)
        m2=heapq.heappop(scoville)
        heapq.heappush(scoville,m1+m2*2)
        answer+=1
    
    if scoville[0]>=K:
        return answer
    else:
        return -1