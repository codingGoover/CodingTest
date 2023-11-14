"""
1989. 초심자의 회문 검사 D2

우아..
문자열 거꾸로 뒤집기 --> string[::-1]
원문 문자열과 비교함 같으면 회문

"""

import sys
sys.stdin= open("../input.txt","r")

def check():
    li = len(word) - 1

    for i in range(len(word) // 2):
        if word[i] != word[li - i]:
            return 0
    return 1

T= int(input())
for t in range(1,T+1):
    word=str(input())
    print("#%d %d"%(t,check()))



