"""
2005. 파스칼의 삼각형 D2

"""
import sys
sys.stdin= open("../input.txt","r")

T= int(input())
for t in range(1,T+1):
    N= int(input())
    pascal=[[1 for j in range(i)] for i in range(1,N+1)]

    for i in range(1,N):
        for j in range(1,i):
            pascal[i][j]= pascal[i-1][j-1]+pascal[i-1][j]

    print("#%d"%t)
    for p in pascal:
        print(*p)