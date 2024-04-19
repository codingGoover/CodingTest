'''
16918번 봄버맨 실버1

문제
https://www.acmicpc.net/problem/16918

'''
import sys
from collections import deque
input=sys.stdin.readline

def main():
    R,C,N= map(int,input().split())
    board=[list(input().rstrip())for _ in range(R)]
    print(*board,sep='\n')
    queue=deque([])
    dr,dc=[0,0,-1,1],[-1,1,0,0]
    
    def bfs():
        while queue:
            r,c=queue.popleft()
            print(r,c)
            board[r][c]='.'
            print(*board,sep='\n')
            for i in range(4):
                nr,nc=r+dr[i],c+dc[i]
                if 0<=nr<R and 0<=nc<C:
                    print(nr,nc)
                    board[nr][nc]='.'
    
    for t in range(1,N+1):
        if t==1:
            for r in range(R):
                for c in range(C):
                    if board[r][c]=='O':
                        queue.append((r,c))
        elif t%2==1:
            bfs()
            for r in range(R):
                for c in range(C):
                    if board[r][c]=='O':
                        queue.append((r,c))
        else:
            board=[['O']*C for _ in range(R)]
    
    for b in board:
        print(''.join(b))
        
main()



# 규칙찾아서 푸는 방식. 
# 짝수초면 무조건 다 폭탄, 
# 홀수초 중 3,7,11,15  / 1,5,9,13,, 이 같은 모양으로 반복됨

import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for i in range(r)]

if n<=1 :
    for li in board : print(''.join(li))
elif n%2==0 :
    for i in range(r): print('O'*c)
else :
    # 첫번째 폭탄이 터진 상태
    bombs1 = [['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x]=='O': bombs1[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and board[y+i][x+j]=='O':
                        bombs1[y][x] = '.'
                        break

    # 두번째 폭탄이 터진 상태
    bombs2 = [['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if bombs1[y][x]=='O' : bombs2[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and bombs1[y+i][x+j]=='O':
                        bombs2[y][x] = '.'
                        break

    if n%4==3:
        for li in bombs1 : print(''.join(li))
    if n%4==1:
        for li in bombs2 : print(''.join(li))
        
'''

1. 변수와 폭탄 정보를 저장한다.

2. n이 1보다 작을 때, 초기 상태를 출력한다.

3. n이 짝수 일 때, 모든 칸을 폭탄으로 출력한다.

4. 위의 경우가 모두 아닐 경우, 첫 번째 폭탄이 터진 상태를 저장하기 위해서는, 전체 칸을 폭탄으로 초기화 시켜놓고 각 칸이 폭탄이거나 상하좌우에 폭탄이 있을 경우 폭탄없음으로 저장한다.

5. 두 번째 폭탄이 터진 상태를 저장하기 위해서는, 전체 칸을 폭탄으로 초기화 시켜놓고 각 칸이 두 번째 폭탄이거나 상하좌우에 두 번째 폭탄이 있을 경우 폭탄 없음으로 저장한다.

6. 3, 7, 11,, 은 4로 나눴을 때 3이 남기 때문에 이 경우 첫번째 폭탄이 터진 상태를 출력하고, 5, 9, 13,, 은 4로 나눴을 때 1이 남기 때문에 이 경우 두번째 폭탄이 터진 상태를 출력한다.

'''