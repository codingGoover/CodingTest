# 1545. 거꾸로 출력해 보아요 D1

'''
주어진 숫자부터 0까지 순서대로 찍어보세요

입력
8

출력
8 7 6 5 4 3 2 1 0

'''

import sys
sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

N = int(input())
for i in range(N,-1,-1):
    print(i, end=' ')