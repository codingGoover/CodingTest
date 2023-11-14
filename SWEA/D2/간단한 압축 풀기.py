"""
1946. 간단한 압축 풀기 D2

출력 줄바꿈 신경쓰기

1
3
A 10
B 7
C 5

#1
AAAAAAAAAA
BBBBBBBCCC
CC

"""
import sys
sys.stdin= open("../input.txt","r")

T= int(input())
for t in range(1,T+1):
    N= int(input())
    zip= [input().split() for _ in range(N)]
    paper=''
    for c,n in zip:
        paper+=c*int(n)

    print("#%d"%t)
    for i in range(len(paper)):
        if i>0 and i%10==0:
            print('\n%c'%paper[i],end='')
        else:
            print(paper[i],end='')
    print()
