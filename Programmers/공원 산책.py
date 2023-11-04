'''
공원 산책 Lv1 

insight 
    >> 단순 구현 문제라는 생각이 드는데
       처음 생각대로 안풀리고 몇번 돌려야 풀린다.. 
       프로그래머스로 이렇게 어떻게 푸는지 적응을 해야하는데 어렵다
문제
https://school.programmers.co.kr/learn/courses/30/lessons/172928

'''
def solution(park, routes):
    answer = []
    N=len(park)  # 세로 N
    M=len(park[0]) # 가로 M
    obstacle=[]
    DIRS={'N':(0,-1),'S':(0,1),'W':(-1,0),'E':(1,0)}
    
    for n in range(N):
         for m in range(M):
             if park[n][m]=='S':
                 x,y=m,n
             elif park[n][m]=='X':
                 obstacle.append((m,n))
    
    for route in routes:
        dx,dy=DIRS[route[0]]
        nx,ny=x,y
        for j in range(int(route[2])):
            nx,ny= nx+dx,ny+dy
            if 0<=nx<M and 0<=ny<N and (nx,ny) not in obstacle:
                flag=True
            else:
                flag=False
                break
        if flag:
            x,y=nx,ny
            #print('x:%d y:%d'%(x,y))
    
    answer.extend([y,x])       
    #print(answer)     
    return answer

solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"])
solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"])
solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"])
