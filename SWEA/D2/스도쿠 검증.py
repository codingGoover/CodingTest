"""
1974. 스도쿠 검증 D2

이차원 리스트 푸는 방법!!
sum([[1,2],[3,4],[5,6],[])

[]+[1,2]+[3,4]+[5,6]
--> [1,2,3,4,5,6]
"""

import sys
sys.stdin= open("../input.txt","r")
T= int(input())

def check():
    # 가로줄 1~9
    for row in sudoku:
        for n in range(1,10):
            if row.count(n)!=1:
                return 0


    # 세로줄 1~9
    for i in range(9):
        col=[sudoku[j][i] for j in range(9)]
        for n in range(1, 10):
            if col.count(n) != 1:
                return 0


    # 사각형 1~9
    for i in range(0,9,3):
        for j in range(0,9,3):
            rect=(sum([sudoku[i+n][j:j+3] for n in range(3)],[]))
            #print(rect)
            for n in range(1, 10):
                if rect.count(n) != 1:
                    return 0

    return 1


for t in range(1,T+1):
    sudoku= [list(map(int,input().split())) for _ in range(9)]
    print("#%d %d"%(t,check()))