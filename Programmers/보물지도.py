'''
[PCCP 모의고사 #2] 4번 - 보물 지도 Lv3

>> 전형적인 BFS 문제
   백준 원숭이,말 이동 유형과 같음
   다시 푸니까 제대로 못풀었음 연습이 더 필요함
   <헷갈렸던 부분>
   장치를 안쓴곳에서 장치를 쓴다면? 조건이므로
   장치를 썼을때 (s+1) visit을 확인해야함. visit[s+1][ny][nx]

'''

from collections import deque
wdx,wdy=[0,0,-1,1],[-1,1,0,0]
sdx,sdy=[0,0,-2,2],[-2,2,0,0]


def solution(n, m, hole):
  
    visit=[[[-1]*n for _ in range(m)] for _ in range(2)]
    # 신발 안씀 0 신발씀 1
    visit[0][m-1][0]=0
    visit[1][m-1][0]=0
    hole = set((a,b) for a,b in hole)  # set,dict in 연산 O(1)
    #print(hole)
    
    queue=deque([(m-1,0,0)])
  

    while queue:
        #print(queue)
        y,x,s=queue.popleft()
      
        if (y,x)==(0,n-1):
            return visit[s][y][x]
        
        for i in range(4):
            nx,ny=x+wdx[i],y+wdy[i]
            if 0<=nx<n and 0<=ny<m and visit[s][ny][nx]== -1 and (nx+1,m-ny) not in hole:
                #print(ny,nx,[nx,m-ny])
                visit[s][ny][nx]=visit[s][y][x]+1
                queue.append((ny,nx,s))
        
        if s==1:
            continue
        
        for i in range(4):
            nx,ny=x+sdx[i],y+sdy[i]
            if 0<=nx<n and 0<=ny<m and visit[s+1][ny][nx]== -1 and (nx+1,m-ny) not in hole:
                visit[s+1][ny][nx]=visit[s][y][x]+1
                queue.append((ny,nx,1))
               
    
    
    return -1