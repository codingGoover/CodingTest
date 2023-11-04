# 1번 중복된 문자 제거 
# my_string='people'
# l= list(my_string)
# print(l)
# d= dict.fromkeys(l)
# print(d)
# list(d) # 키만 가지고옴
# print(''.join(d))


'''
안전지대 Lv0

문제
https://school.programmers.co.kr/learn/courses/30/lessons/120866

insight 
    >> 나랑 생각을 반대로,,
       지뢰가 아닌 곳에서 8방향 돌려 지뢰가 보이면 
       지뢰 주변자리이므로 0으로 전환
       
       8방향 저장 헷갈리지말게
'''

DIRS=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def solution(board):
    answer = 0
    N= len(board)
    
    #처음부터 1로 채워진 같은 사이즈의 보드
    arr=[[1 for _ in range(N)]for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if board[r][c]: # 1은 True
                arr[r][c]=0
                continue
            
            # 8 방향 탐색
            for dr, dc in DIRS:
                nr, nc= dr+r , dc+c
                
                # 유효한 좌표인지 확인
                if nr<0 or nr>=N or nc<0 or nc>=N : # out of index
                    continue
                
                if board[nr][nc]: #지뢰가 존재하는지
                    arr[r][c]=0
                    continue
                
    print(*arr, sep='\n')            
    return sum([sum(a) for a in arr])
    
solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])