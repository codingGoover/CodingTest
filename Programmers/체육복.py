'''
체육복 Lv1 탐욕법(Greedy)

문제
https://school.programmers.co.kr/learn/courses/30/lessons/42862

'''
def solution(n, lost, reserve):

    wear=[1]*n
    
    for i in lost:
        wear[i-1]-=1
        
    for i in reserve:
        wear[i-1]+=1
    
    for i in range(n):
        
      if wear[i]>1:
            for l in (i-1,i+1):
                if 0<=l<n and wear[l]==0:
                    wear[l]+=1
                    wear[i]-=1
                    break
                    
            if wear[i]>1:
                wear[i]=1
        #print(i,wear)           
        
    return sum(wear)