"""
1979. 어디에 단어가 들어갈 수 있을까 D2

>> 생각의 전환. cnt값 체크를 경계부분인 벽에서 하면 간단하다. 경우가 줄어든다

"""
import sys
sys.stdin= open("../input.txt","r")

T= int(input())
for t in range(1,T+1):
    N,K= map(int,input().split())
    puzzle=[list(map(int,input().split())) for _ in range(N)]
    result=0

    for i in range(N):
        cnt,flag=0,False
        for j in range(N):
            if not cnt and puzzle[i][j] and not flag:
                flag=True
                cnt+=1
            elif flag and puzzle[i][j]:
                cnt+=1
                if cnt==K:
                    result+=1
                if cnt>K:
                    result-=1
                    flag = False
            elif not puzzle[i][j]:
                flag=False
                cnt=0

    for j in range(N):
        cnt, flag = 0, False
        for i in range(N):
            if not cnt and puzzle[i][j] and not flag:
                flag = True
                cnt += 1
            elif flag and puzzle[i][j]:
                cnt += 1
                if cnt == K:
                    result += 1
                if cnt > K:
                    result -= 1
                    flag=False
            elif not puzzle[i][j]:
                flag = False
                cnt = 0

    print("#%d %d"%(t,result))



# 똑똑한 코드 : 벽을 만났을 때 count를 계산하라 !
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        count = 0
        # 행검사
        for j in range(n):
            if puzzle[i][j] == 1:
                count += 1
            if puzzle[i][j] == 0 or j == n - 1:
                if count == k:
                    answer += 1
                count = 0

        # 열검사
        for j in range(n):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == n - 1:
                if count == k:
                    answer += 1
                count = 0
    print(f"#{test_case} {answer}")
