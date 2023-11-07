
'''
9663번 N-Queen 골드4

insight
    >> queen의 좌표를 일차원리스트로 저장해야 시간초과가 절대 안남
       (x,y) 좌표 자체를 튜플 리스트로 저장했는데 시간초과 다뜸
 
문제
https://www.acmicpc.net/problem/9663

예제 입력 1 
8
예제 출력 1 
92
      
'''
import sys
input=sys.stdin.readline

def check(y):
    
    for yy in range(y):
        if queen[y]==queen[yy] or y-yy == abs(queen[y]-queen[yy]):
            return False
    
    return True    


def dfs(y):
    global cnt
    
    if y==N:
        if len(queen)==N:
            cnt+=1
        return
    
    for nx in range(N):  
        queen[y]=nx     
        if check(y):
            #print(queen)
            dfs(y+1)
            
    
    
    
# N x N 체스판 퀸 N개
N= int(input())
queen=[0]*N
cnt=0

dfs(0)
print(cnt)
