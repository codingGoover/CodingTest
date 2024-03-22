'''
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 
Lv3 다단계 칫솔 판매
>> 끝에 테케3개는 질문게시판보고 알았음
'''

from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
      
    answer=defaultdict(int)
    people=dict(zip(enroll,[i for i in range(len(enroll))]))
    
    def dfs(name,money):
        
        #분배금이 0인 경우면 return 해야함,,
        if name=='-' or money==0:
            return 
        
        remain =math.floor(money*0.1)
        #print(name,money,remain)
        
        answer[name]+=money-remain
        
        #print(answer)
    
        dfs(referral[people[name]],remain)
    
    
    for idx,name in enumerate(seller):
        dfs(name,amount[idx]*100)

        
    return [answer[n] for n in enroll]