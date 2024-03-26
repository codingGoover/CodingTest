'''
9017번 크로스 컨트리 실버3

insight
>> 끝까지 돌아가야 틀리지 않음.
   이정도 숫자범위에서는 시간복잡도에 부담을 느끼지 말것,,

입력범위 N (6 ≤ N ≤ 1,000)

'''

import sys
from collections import defaultdict
input=sys.stdin.readline

T= int(input())
for _ in range(T):
    N= int(input())
    seq=list(map(int,input().split()))
    team=set(seq)
    rank = dict()

    '''
    for t in team:
        if seq.count(t)==6:
            rank[t]=[0,0]
        else:
            rank[t]=[-1,-1]
    
    ans= dict()
    
    score=1
    for r in seq:
       
        if rank[r]==[-1,-1]:
            continue
        
        rank[r][1]+=1
         
        if rank[r][1]<=4:
            rank[r][0]+=score
        
        if rank[r][1]==4:
            ans[r]=[rank[r][0],-1]
        
        elif rank[r][1]==5:
            ans[r][1]=score
        
        score+=1
        
    if len(ans)==1:
        print(list(ans.keys())[0])
    else:
        print(sorted(ans.items(),key=lambda x: (x[1][0],x[1][1]), reverse=False)[0][0])
    
    '''
                    
    # 찾아보고 고친코드인데 그렇게 시간차이안남 ㅡ.ㅡ
    rank=dict()
    
    for t in team:
            if seq.count(t)==6:
                rank[t]=[0,0,0]
    score=1 
    for s in seq:
        
        if rank.get(s,-1)==-1:
            continue
        
        if rank[s][0]<4:
            rank[s][0]+=1
            rank[s][1]+=score
        elif rank[s][0]==4:
            rank[s][0]+=1
            rank[s][2]=score
        
        score+=1

    #print(rank)
    print(sorted(rank.items(),key=lambda x:(x[1][1],x[1][2]),reverse=False)[0][0])


'''
https://itstime0809.tistory.com/4
또 다른코드 이거는 좀더 빠름 
그냥 개짱남
'''
