'''
추억 점수 Lv1

문제
https://school.programmers.co.kr/learn/courses/30/lessons/176963


key: listA    value: listB
d= dict(zip(listA,listB))

'''
from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    score= {}
    for i in range(len(name)):
            score[name[i]]=yearning[i]
           
    for plist in photo:
        answer.append(0)
        for p in plist:
            if p in score.keys():
                answer[-1]+=score[p]
   
    return answer

# 더 짧은 코드 
def solution(name, yearning, photo):
    answer = []
    d= defaultdict(int, zip(name,yearning))
    for p in photo:
        # ["may", "kein", "kain", "radi"] --> [5,10,1,3] --> 19
        answer.append(sum([d[u] for u in p]))
    
    return answer