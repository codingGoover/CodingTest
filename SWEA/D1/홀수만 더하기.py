'''
2072. 홀수만 더하기 D1

10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

[제약 사항]

각 수는 0 이상 10000 이하의 정수이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
 
출력
#1 200
#2 208
#3 121

'''
import sys
sys.stdin=open("../input.txt", "r")
input=sys.stdin.readline


T= int(input())
for test_case in range(1,T+1):
    num=list(map(int,input().split()))
    ans=0
    for n in num:
        if n%2>0:
            ans+=n
    print('#%d %d'%(test_case,ans))

"""
1545 거꾸로 출력해보아요 D1
>> in range(5,-1,-1)  5 4 3 2 1 0
>> in range(5 0,-1)   5 4 3 2 1   

"""
N=int(input())
for n in range(N,-1,-1):
    print(n,end=' ')


# 2047 신문 헤드라인 D1
# >> 대문자로 바꿔서 반환해주는 함수 str.upper()
string= str(input())
print(string.upper())

# 스탬프찍기
# >> 같은 문자열 반복 이어붙이기 python : *
N= int(input())
print("#"*N)


