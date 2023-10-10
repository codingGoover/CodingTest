'''
15663번 N과 M(9) 실버2

insight
    >> 재귀 호출 전, 방문할 숫자 = 이전값(prev)을 기억하여 
       그 다음턴때 중복된 숫자인지 아닌지 체크한다. 
       변수 저장과 비교 위치가 중요함...

문제
https://www.acmicpc.net/problem/15663

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4

예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 7
1 9
7 1
7 9
9 1
9 7
9 9

예제 입력 3 
4 4
1 1 1 1
예제 출력 3 
1 1 1 1

예제 입력 4
6 3
1 4 4 5 5 6
예제 출력 4
1 4 4
1 4 5
1 4 6
1 5 4
1 5 5
1 5 6
1 6 4
1 6 5
4 1 4
4 1 5
4 1 6
4 4 1
4 4 5
4 4 6
4 5 1
4 5 4
4 5 5
4 5 6
4 6 1
4 6 4
4 6 5
5 1 4
5 1 5
5 1 6
5 4 1
5 4 4
5 4 5
5 4 6
5 5 1
5 5 4
5 5 6
5 6 1
5 6 4
5 6 5
6 1 4
6 1 5
6 4 1
6 4 4
6 4 5
6 5 1
6 5 4
6 5 5

'''

import sys
input=sys.stdin.readline

def dfs(len,sequence):
    prev=0
    
    if len==M:
        print(*sequence)
        return
    
    for i in range(N):
        if not visited[i] and prev!=number[i]:
        
            visited[i]=True
            sequence.append(number[i])
            prev=number[i]
            
            dfs(len+1,sequence)
            
            visited[i]=False
            sequence.pop()       

N,M= map(int,input().split())

number=sorted(map(int,input().split()))
# nset= sorted(set(number))

# for i in nset:
#     visited=[False]*N
#     visited[number.index(i)]=True    
#     dfs(1,[i])
    
visited=[False]*N
dfs(0,[])


# 모든 수열값을 넣고 set으로 중복제거하는 방식 --> 1.5배가 걸리지만 정답처리 됨
# if len(arr) == m:
#    answers.append(arr[:]) # 정답 리스트에 추가
#    return

# answers = sorted(list(set(map(tuple, answers))))