'''
대충 만든 자판 Lv1

문제
https://school.programmers.co.kr/learn/courses/30/lessons/160586

>> dict.get(key, 키가없을때 뱉는 값)
   defaultdict(lambda: 초기값)  딕셔너리 초기값 설정가능 

'''
from collections import defaultdict


def solution(keymap, targets):
    answer = []
    keyDict={}
    
    for key in keymap:
        for i,k in enumerate(key):
            keyDict[k]=min(keyDict.get(k,100),i+1)
    
    print(keyDict)
    
    # for target in targets:
    #     sum=0
    #     for t in target:
    #         if t not in keyDict.keys():
    #             sum=-1
    #             break
    #         sum+=keyDict[t]
    #     answer.append(sum)
    
    for target in targets:
        li= [keyDict.get(t,-1) for t in target]
        if min(li)<0:
            answer.append(-1)
        else:
            answer.append(sum(li))
          
       
    return answer

def solution(keymap, targets):
    answer = []

    # 다른 코드 
    d= defaultdict(lambda: 101)  #c초기값 lambda로 설정
    for k in keymap:
        # 'ABACD' -> 'A','B' ...
        for idx,c in enumerate(k):
            d[c]= min(d[c],idx+1)

    for t in targets:
        total=0
        available=True
        
        # "ABCD"
        for c in t:
            if c in d:
                total +=d[c]
            else:
                available=False
                break
                
        if available:
            answer.append(total)
        else:
            answer.append(-1)

    return answer