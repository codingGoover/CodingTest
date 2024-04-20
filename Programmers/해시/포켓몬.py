'''
고득점Kit 해시 포켓몬 Lv1 

'''

from collections import defaultdict
def solution(nums):
    answer = 0
    pick=defaultdict(int)
    
    
    for n in nums:
        if len(pick)< len(nums)//2:
            if pick[n]==0:
                pick[n]=1
    
    #print(pick)
    
    return len(pick)