'''
2019. 더블더블 D1

>> 2 ** 3 == 8
   제곱 연산자
'''
import sys
sys.stdin= open("../input.txt","r")
input=sys.stdin.readline

N= int(input())
for i in range(N+1):
    print(2**i, end=' ')