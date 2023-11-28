'''
PCCP 모의고사1회 2번
Lv2 DFS 
'''
answer = 0
def solution(ability):
    
    N=len(ability)
    n=len(ability[0])
    visit=[False]*N
    
    def dfs(ssum,pick):
        global answer 
        
        if pick==n:
            answer=max(ssum,answer)
            return
        
        for i in range(N):
            if not visit[i]:
                visit[i]=True
                dfs(ssum+ability[i][pick],pick+1)
                visit[i]=False
            
    dfs(0,0)
    
    return answer