'''
신고 결과 받기 Lv1

문제
https://school.programmers.co.kr/learn/courses/30/lessons/92334

>> set()을 활용해서 애초에 중복을 제거하는 것을 생각하면 쉬워짐
   setA.add()
'''

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    users=defaultdict(set)
    banned= defaultdict(int)
    
    # 중복된 신고처리 제거
    report= set(report)
    
    for re in report:
        a,b= re.split()
        users[a].add(b)
        banned[b]+=1
    
    for id in id_list:
        sum=0
        for p in users[id]:
            if banned[p]>=k:
                sum+=1
        answer.append(sum)
    
    # 한줄로 나타내기
    for id in id_list:
        answer.append(sum([ 1 for u in users[id] if banned[u]>=k]))
        
        
    
    return answer