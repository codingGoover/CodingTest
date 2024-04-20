'''
기능개발 Lv2

스택큐라 해가지구 큐라고 풀었는데
실전에서는 ..? 그리고 날짜 계산 이런거 똑바로 해야함 올림해주는거 잊으면 안됨 

'''

from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    progresses=deque(progresses)
    speeds=deque(speeds)
    
    while len(progresses)>0:
        days= math.ceil((100-progresses[0])/speeds[0])    
        # 나머지있으면 올림해줘야하는데, 날짜계산 똑바로 안해서 틀림
        idx=0
        
        for i in range(1,len(progresses)):
            progresses[i] += speeds[i]*days
            
            if progresses[i]>=100:
                if i-idx==1:
                    idx+=1
        # print(idx)
        # print(progresses)
        for i in range(1+idx):
            progresses.popleft()
            speeds.popleft()
            
        answer.append(1+idx)
        
    days=[]
    for p,s in zip(progresses,speeds):
        days.append(math.ceil((100-p)/s))
    
    return answer




# 다시 푼 날짜만 이용해서 푸는 방법
from collections import deque
import math
def solution(progresses, speeds):
    answer=[]
    
    days=[]
    for p,s in zip(progresses,speeds):
        days.append(math.ceil((100-p)/s))
    
    while len(days)>0:
        cnt=1
        
        for d in days[1:]:
            if d<= days[0]:
                cnt+=1
            else:
                break
        
        days=days[cnt:]
        answer.append(cnt)
    
    return answer



'''
기준점 포인트를 따로 저장하는 좋은 방식! 제일빠름 조음
 
 progresses 의 각 소요시간을 확인하는데 
 이때 front 에 가장 오래걸린 소요 시간의 인덱스를 저장해둔다. 

우선 초기값으론 0인덱스 

 

3) idx = 0 : 첫번째 수(7) 보다 첫번째 수 (7) 는 같기 때문에 pass ==> front = 0

4) idx = 1 : 첫번째 수(7) 보다 두번째 수(3) 는 작기 때문에 pass ==> front = 0

5) idx = 2 : 첫번째 수(7) 보다 세번째 수(9) 는 크기 때문에 

         - 현재 인덱스부터 프론트인덱스의 차를 구하고 이를 answer에 append (그 전까지 친구들은 동시 출시니까)

         - 프론트인덱스를 현재인덱스로 업데이트! ==> front = 2

---- 반복문 완료 ---

6) 맨 마지막에 현재 프론트인덱스와 전체 길이의 차를 구해서 남은 친구들 다 출시 
'''

def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0     # 더 기다려야하는 맨 첫시작을 지정해두고

    for idx in range(len(progresses)):
        
        if progresses[idx] > progresses[front]:  
            print(progresses, idx,front)
            answer.append(idx - front)
            front = idx 
            
    answer.append(len(progresses) - front)  

    return answer