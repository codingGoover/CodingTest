'''
1182번 부분수열의 합 실버2

insight
    >> 수열합이 양인 경우 음인 경우
       나누어 생각해서 조건문을 더 걸어주었지만 
       아무것도 없는게 오히려 더 시간이 적게 걸렸다. 20ms ↓ 
       굳이 굳이 시간 줄이고자 더 고민할 필요가 없었던 문제 허무하다
       
       백트래킹 하나하나 해도 시간초과 X 
       단순하게 생각하자. . 실버2
    
문제
https://www.acmicpc.net/problem/1182

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.


7 0
-7 -3 -2 -1 1 5 8
6

5 0
0 0 0 0 0
31

5 0
0 0 0 1 0
15

5 0 
1 2 3 4 5
0

6 6
1 2 3 4 5 6
4

5 -2
-1 -1 -1 -1 -1
10

15 -7
6 -4 1 3 -8 5 -4 -3 7 -4 9 -9 -3 -4 -4
1203

4 -6
2 -9 -2 -6
2

4 -12
-6 3 -3 -3
1

8 22
10 8 -6 6 0 10 5 3
6

5 5
3 2 1 2 3
5

'''

import sys
input=sys.stdin.readline

def dfs(sum,idx):
    
    global cnt
    
    if sum==S:
        cnt+=1
    
    for i in range(idx+1,N):
        #if not (S<sum+number[i]) or S<sum+number[i]<0 : 
            sum+=number[i]
            dfs(sum,i)
            sum-=number[i]
            
# 정수 개수 N 부분수열합 S
N,S= map(int,input().split())
number=sorted(map(int,input().split()))
cnt=0


for i in range(N):
    if (0<=number[i]<=S) or not (number[i]>=0>S) :
        dfs(number[i],i)

print(cnt)

