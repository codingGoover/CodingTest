"""
1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3

>> 푸는데 너무 오래걸렸던 문제 ,, 내가 생각한 방식도 결국엔 한계가 있었음
   백트래킹? 숫자 하나하나에 visit을 주는 것이 아닌
   (숫자열 전체, 층) 을 하나로 묶어 visit 처리가 필요하다.
   왜냐하면 카드를 swap할수있는 기회(chance)는 최종 최대값을 만들수있는 방법보다 더 클수도 있기때문
   카드를 한장씩 바꾸는 경우는 조합을 생각하여 이중 반복문이면 모든걸 만들 수있었음......
   for A in range(숫자길이):
    for B in range(A+1,숫자길이):
        A,B = B,A

"""

import sys
sys.stdin= open("../input.txt","r")


def dfs(cnt):
    global answer
    if cnt == 0:
        answer = max(int("".join(num)), answer)
        return

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            number = int("".join(num))
            if (number, cnt) not in visit:
                visit.append((number, cnt))
                dfs(cnt - 1)
                # visit.remove(number)
            num[i], num[j] = num[j], num[i]


T = int(input())

for t in range(1, T + 1):
    num, change = map(int, input().split())
    num = list(str(num))
    answer = 0
    visit = []
    dfs(change)
    print(f'#{t} {answer}')


# 글러먹은 내코드
# def dfs(idx,cnt):
#     global score
#     #print(cnt)
#
#     if cnt==chance:
#         score= max(int(''.join(number)),score)
#         #print(score)
#         return
#
#     for i in range(L):
#         if not visited[i]:
#             number[idx],number[i]=number[i],number[idx]
#             visited[i]=True
#             #print(idx,i, number)
#             dfs(idx+1,cnt+1 if idx!=i else cnt)
#             visited[i]=False
#             number[idx], number[i] = number[i], number[idx]
#             #print("--",idx, number)
#
# T= int(input())
# for t in range(1,T+1):
#     number,chance=map(str,input().split())
#     chance=int(chance)
#     score=0
#     number,L=list(number),len(number)
#     visited=[False]*L
#
#     dfs(0,0)
#
#     print(f'#{t} {score}')
#
