'''
5073번 삼각형과 세 변 브론즈3

>> 그냥 조건문 문제,,
'''

import sys
input=sys.stdin.readline

while True:
    arr=list(map(int,input().split()))
    if sum(arr)==0:
        break
    
    arr.sort(reverse=True)
    
    if arr[0]< arr[1]+arr[2]:
        if arr[0]==arr[1]==arr[2]:
            print('Equilateral')
        elif arr[0]==arr[1] or arr[1]==arr[2]:
            print('Isosceles')
        else:
            print('Scalene')
    else:    
        print('Invalid')
    
        
    
    