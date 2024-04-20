'''
같은 숫자는 싫어 Lv1

스택,큐 문제인걸 몰랐어도
이렇게 풀었을까? 아무튼 끝에 값 비교하는건 스택으로 생각하면 쉬움
'''

def solution(arr):
    
    stack=[]
    
    for a in arr:
        if len(stack)>0:
            if stack[-1]!=a:
                stack.append(a)
        else:
            stack.append(a)
    
    return stack