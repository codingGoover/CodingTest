''' 
깊이우선탐색 (DFS) 공부

예시 그래프

  0
 /
1 ― 3  
| / | \ 
2 ― 4  5 ― 7
        \ 
         6 ― 8 
   
 
구현1) 순환함수 이용  
startX 0 dfs(1)
startX 1 dfs(2)
startX 2 dfs(3)
startX 3 dfs(4)
back 3
startX 3 dfs(5)
startX 5 dfs(6)
startX 6 dfs(8)
back 6
back 5
startX 5 dfs(7)
back 5
back 3
back 2
back 1
back 0

방문순서
--> 0 1 2 3 4 5 6 8 7

구현2) Stack 이용
bfs구현방식에서 queue 가 아니라 stack으로 구현

방문순서
--> 0 1 3 5 7 6 8 4 2

참고
https://www.youtube.com/watch?v=_hxFgg7TLZQ  

'''

from collections import deque

# 방법1) 순환 호출을 이용 
 
def dfs(startX):
    visted[startX]=True
    print('%d' %startX, end=' ')   # 방문 노드 순서 출력 
   
    for x in graph[startX]:
        if not visted[x]:
            #print('startX %d dfs(%d)'%(startX,x)) startX에서 dfs(x)를 호출
            dfs(x)
            #print('back %d'%startX)    #bfs() 끝나고 돌아온(올라온) 지점
    
visted=[False]*9 
graph=[[1],
       [0,2,3],
       [1,3,4],
       [1,2,4,5],
       [2,3],
       [3,6,7],
       [5,8],
       [5],
       [6]]

dfs(0)
print()



# 방법2) 명시적인 스택 사용 - 스택에 인접노드를 모두 넣고 방문하는 방식

def stackDFS(startX):
    visted[startX]=True
    stack=deque([startX])
    
    while stack:
        x= stack.pop()
        print('%d' %x, end=' ') # 방문 노드 출력 순서 
        for i in graph[x]:
            if not visted[i]:
                stack.append(i)
                visted[i]=True


visted=[False]*9 
stackDFS(0)     