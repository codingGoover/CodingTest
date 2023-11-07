'''
16987번 계란으로 계란치기 골드5

insight
    >> return 조건이 중요했던 문제 
       왼쪽 계란을 끝까지 무조건 돌아야하고 최댓값은 최종 cnt(==왼쪽계란을 끝까지 들고 내린 후)만 비교하여 고르면됨
       백트래킹은 맞게했는데 조건을 다 제대로 못줬음

문제
https://www.acmicpc.net/problem/16987


'''

import sys
input=sys.stdin.readline

def dfs(i,cnt):
    global ans
    temp=0
 
    if i==N:
        ans= max(cnt,ans)
        return
   
    eggS,eggW= egg[i]
   
    if eggS<=0 or cnt==N-1:
        dfs(i+1,cnt)
        return
    
    for j in range(0,N):
        
        neggS,neggW= egg[j]

        if j==i or neggS<=0:
            continue
            
        #print('temp= %d for j %d' % (temp,j))
        egg[i][0]-=egg[j][1]
        egg[j][0]-=egg[i][1]
        
        #새로운 계란만 깨짐
        if egg[j][0]<=0:
            temp+=1
            #print("broke right %d egg"%j)
        
        #기존 계란이 깨짐
        if egg[i][0]<=0:
            temp+=1
            #print("broke left %d egg"%i)
            
        #print(egg,temp)
        dfs(i+1,cnt+temp)
        egg[i][0]+=neggW
        egg[j][0]+=eggW
        temp=0
            
                  




# 계란의 수 N
N= int(input())

# 내구도 S 무게 W
egg=[list(map(int,input().split()))for _ in range(N)]
#broken=[False]*(N)
ans=0

#print(egg)

dfs(0,0)

print(ans)


