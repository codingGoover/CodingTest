'''
20125번 쿠키의 신체 측정 실버4

insight
>> 그냥 구현 문제

5 ≤ N ≤ 1,000
최대복잡도 1000 * 1000

'''

import sys
input=sys.stdin.readline

N= int(input())
board= [list(input().rstrip())for _ in range(N)]
#print(*board,sep='\n')
head=tuple()
for i in range(N):
    for j in range(N):
        if board[i][j]=='*':
            head=(i,j)
            break
    if len(head)>0:
        break

# 행,열
heart=(head[0]+1,head[1])
#print(head, heart)
left_arm=board[heart[0]][:heart[1]].count('*')
right_arm=board[heart[0]][heart[1]+1:].count('*')
body=0

for r in range(heart[0]+1,N):
    if board[r][heart[1]]=='*':
        body+=1
    else:
        break

left_leg=0
right_leg=0

for r in range(heart[0]+body+1,N):
    if board[r][heart[1]-1]=='*':
            left_leg+=1
    if board[r][heart[1]+1]=='*':
            right_leg+=1
    
    if board[r][heart[1]-1]==board[r][heart[1]+1]=='_':
        break

print(f'{heart[0]+1} {heart[1]+1}')
print(f'{left_arm} {right_arm} {body} {left_leg} {right_leg}')