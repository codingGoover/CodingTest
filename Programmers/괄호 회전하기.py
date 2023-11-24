"""
괄호 회전하기 Lv2

>> stack 활용하기 ,
   deque의 rotate(N) 활용 해봄
   N>0 : 오른쪽으로 회전
   N<0:  왼쪽으로 회전

"""

from collections import deque

couple = {']': '[', '}': '{', ')': '('}

def solution(s):
    answer = 0
    dq = deque(s)
    for i in range(len(s)):
        dq.rotate(-1)
        left = []
        flag = True
        for d in dq:
            if d in ['[', '{', '(']:
                left.append(d)
            else:
                if len(left) == 0:
                    flag = False
                    break
                elif left[-1] == couple[d]:
                    left.pop()
                else:
                    flag = False
                    break

        if flag and len(left) == 0:
            answer += 1

    return answer