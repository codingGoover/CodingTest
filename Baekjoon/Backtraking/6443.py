'''
6443번 애너그램 골드5

insight
    >> 백트랙킹, prev변수 + 일차원리스트 visited
       앞전 N과 M 중복숫자 나온 경우와 유사해보여 
       prev변수로 이전값을 기억해 최종단어 중복체크함
    
       찾아보니 최종단어 중복체크를 딕셔너리visited로도 가능 굿

문제
https://www.acmicpc.net/problem/6443

예제 입력 1 
2
abc
acba

예제 출력 1 
abc
acb
bac
bca
cab
cba
aabc
aacb
abac
abca
acab
acba
baac
baca
bcaa
caab
caba
cbaa

'''
import sys
input=sys.stdin.readline

def dfs(anagram):
    
    prev='~'
    
    if len(anagram)==len(word):
        print(''.join(anagram))
        return
    
    for i in range(0,len(word)):
        if not visited[i] and prev!=word[i]:
            visited[i]=True
            anagram.append(word[i])
        
            dfs(anagram)
            visited[i]=False
            anagram.pop()
            prev=word[i]
    

# 단어의 개수 N
N= int(input())

for _ in range(N):
    word=sorted(map(str,input().rstrip()))
    visited=[False]*len(word)
    dfs([])


#-----------------------------------------------------------------------#
# vistied를 딕셔너리이용 key: value -> {문자: 문자개수} 으로 중복된 문자가 있더라도 중복된 단어 체크가능 훨씬 간단한 사고 (시간 ↓  메모리 ↑ 유의미한 차이는 X)
# 15663번 N과M 문제도 이방식으로 가능 + 코드 추가함

import sys


def back_tracking(cnt):

    # 현재 문자 길이가 입력된 문자 길이와 같다면 출력
    if cnt == len(word):
        print("".join(answer))
        return

    # 반복문을 통해 visited에 단어를 확인
    for k in visited:
        if visited[k]: # 0 이 아닌 수이면
            visited[k] -= 1 # k를 사용할 것으로 -1
            answer.append(k) # answer에 더해준다.
            back_tracking(cnt + 1) # 백트래킹
            visited[k] += 1 # k를 사용안한 것으로 +1
            answer.pop() # answer에서 빼준다.


n = int(sys.stdin.readline())

for _ in range(n):
    word = sorted(list(map(str, sys.stdin.readline().strip())))
    visited = {}
    answer = []

    # 반복문을 통해 visited에 알파벳의 개수를 입력
    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    # 백트래킹
    back_tracking(0)