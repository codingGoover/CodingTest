'''
최빈값 구하기 Lv0

문제
https://school.programmers.co.kr/learn/courses/30/lessons/120812

>> max(최댓값 찾을곳, key= lambda x: 최댓값찾을곳의 기준)
'''

from collections import defaultdict
def solution(array):
    answer = -1
    d= defaultdict(int)
    for a in array:
        d[a]+=1
    
    maxKey= max(d,key=lambda x:d[x])
    answer= maxKey
    
    for k,v in d.items():
        if maxKey!=k and v==d[maxKey]:
            answer=-1
            break
    
    return answer