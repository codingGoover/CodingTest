'''
올바른 괄호 Lv2 스택

분명 두번은 더 풀었던 문제임 
왜왜 도대체 왜!!! 생각을 너무 조급하게함 
다시 찾은 코드
스택 2개로 안만들어도됨
'''

def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
