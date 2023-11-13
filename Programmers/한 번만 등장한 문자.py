'''
한 번만 등장한 문자 Lv0

문제
https://school.programmers.co.kr/learn/courses/30/lessons/120896

>> defaultdict 을 알게됨

'''

from collections import defaultdict

def solution(s):
    answer = ''
    alpha=defaultdict(int)    
    
    for c in s:
        alpha[c]+=1
        
    for k,v in alpha.items():
        if v==1:
            answer+=k
    
    return ''.join(sorted(answer))

