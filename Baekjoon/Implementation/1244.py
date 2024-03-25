'''
1244번 스위치 개수 실버4

insight
>> 간단 구현문제 숫자가 좀 헷갈림
   N배수 만들기 
   for in range(N, 끝수+1, N)

입력 스위치 개수 100 이하 

'''
import sys
input=sys.stdin.readline

switchN=int(input())
switch=list(map(int,input().split()))
peopleN=int(input())

for _ in range(peopleN):
    gen,num=map(int,input().split())
    if gen==1:
        for i in range(num,switchN+1,num):   # num 배수만큼 수범위찾는것
            switch[i-1]= 0 if switch[i-1] else 1
    
    else:
        num-=1
        for i in range(switchN//2+1):
            if num-i<0 or num+i>switchN-1:
                break
            if switch[num-i]==switch[num+i]:
                switch[num+i]=switch[num-i]= 0 if switch[num-i] else 1
            else:
                break
    #print(switch)


for i in range(switchN):
    print(switch[i],end=' ')
    if (i+1)%20==0:
        print()
