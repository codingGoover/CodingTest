'''
고득점 KIT 해시 완주하지 못한 선수 LV1

collections의 Counter

>>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
Counter({'hi': 3, 'hey': 2, 'hello': 1})

'''

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 내풀이
from collections import defaultdict
def solution(participant, completion):
    answer = ''
    runner=defaultdict(int)
    
    for c in completion:
        runner[c]+=1
    
    for p in participant:
        if runner[p]<=0:
            return p
        runner[p]-=1
        
    return answer