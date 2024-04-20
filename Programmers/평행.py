'''
평행 Lv0  코딩입문 구현

>> DFS로 선정해서 풀어봄

'''

answer=0
def solution(dots):
    
    visit=[False]*4
    
    def dfs(a,b):
        global answer
        dot1=[]
        dot2=[]
        
        if b!=-1:
            for idx in range(4):
                if idx in [a,b]:
                    dot1.append(dots[idx])
                else:
                    dot2.append(dots[idx])
                    
            lean1=(dot1[0][0]-dot1[1][0])/(dot1[0][1]-dot1[1][1])
            lean2=(dot2[0][0]-dot2[1][0])/(dot2[0][1]-dot2[1][1])
            print(lean1,lean2)
            
            if lean1==lean2:
                return 1
            else:
                return 0
        
        for j in range(4):
            if not visit[j]:
                visit[j]=True
                if dfs(a,j)==1:
                    answer=1
                    break
    
    visit[0]=True
    dfs(0,-1)
   
    return answer
                
    
    
    
    
