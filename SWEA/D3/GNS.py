"""
1221. [S/W 문제해결 기본] 5일차 - GNS D3
"""
import sys
sys.stdin= open("../input.txt","r")
strD={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
numD={0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
T= int(input())
for t in range(1,T+1):
    case,len=input().split()
    arr= list(input().split())
    number=[strD[a] for a in arr]
    number.sort()

    print(case)
    for n in number:
        print(numD[n],end=' ')
    print()

# 정렬하지말고 숫자 개수를 세서 낮은 숫자부터 개수 만큼 출력하면 됨