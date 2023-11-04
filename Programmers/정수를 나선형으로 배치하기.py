'''
정수를 나선형으로 배치하기 Lv0

insight
    >> 지연이는 노가다 방식
    
'''
def solution(n):
    answer = [[0]*n for _ in range(n)]
    end=n-1
    num=1
    i,j=0,0
    
    while end>0:
        for _ in range(end):
            answer[i][j]=num
            num+=1
            j+=1
            
        for _ in range(end):
            answer[i][j]=num
            num+=1
            i+=1
            
        for _ in range(end):
            answer[j][i]=num
            i-=1
            num+=1
       
        for _ in range(end):
            answer[j][i]=num
            num+=1        
            j-=1
        
        end-=2
        i+=1
        j+=1
        
        print(*answer,sep='\n')
        print()
    
    if answer[i][j]==0:
        answer[i][j]=n*n
     
    return answer

print(*solution(5),sep='\n')




# 강사 코드 
DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
 
class Number:
    val, direction, r, c = 1, 0, 0, 0
    
    def __init__(self, board):
        board[self.r][self.c] = self.val # (0,0) <= 1
        
    def move(self, board):
        dr, dc = DIRS[self.direction]
        nr, nc = self.r + dr, self.c + dc
        
        if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board) or board[nr][nc] != 0:
            self.direction = (self.direction + 1) % 4
            dr, dc = DIRS[self.direction]
            nr, nc = self.r + dr, self.c + dc
        
        self.val += 1
        self.r, self.c = nr, nc
        board[self.r][self.c] = self.val
        
def solution(n):
    answer = []
    for _ in range(n):
        answer.append([0] * n)
    
    num = Number(answer)
    
    for _ in range(n * n - 1):
        num.move(answer)
    
    return answer

