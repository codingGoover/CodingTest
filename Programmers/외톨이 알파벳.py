'''
[PCCP 모의고사 #1] 1번 - 외톨이 알파벳 Lv1
>> 문자열

'''
def solution(input_string):
    answer = ''
    alpha={}
    for idx,c in enumerate(input_string):
        if alpha.get(c,0)==0:
            alpha[c]=[idx]
        else:
            alpha[c].append(idx)
    
    for key in alpha:
        if len(alpha[key])>=2:
            for i in range(len(alpha[key])-1):
                if alpha[key][i+1] - alpha[key][i]>1:
                    answer+=key
                    break
                    
    
    return ''.join(sorted(answer)) if answer!='' else 'N'


# 더 간단한 방법 prev와 cur 변수를 활용

from collections import defaultdict
def solution(input_string):
    answer=''
    sH=defaultdict(int)
    prev=None
    for cur in input_string:
        if cur!=prev:
            sH[cur]+=1
        prev=cur
    for key,val in sH.items():
        if val>=2:
            answer+=key
            
    if len(answer)==0:
        return 'N'
    
    return ''.join(sorted(answer))