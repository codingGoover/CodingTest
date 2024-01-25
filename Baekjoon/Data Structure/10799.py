'''
10799번 쇠막대기 실버2

insight
    >> 스택활용인데 잘 활용했는지 모르겠지만 규칙을 찾아서 푼 문제 
       --> 다른 코드 찾아보니 맞았음! 
       채점시간이 오래걸려서 시간초과 나려나 했지만 통과함 질문게시판보니 시간초과 사례 많음
       
       첫 번째, 먼저 그림을 보면서 규칙을 찾아 보면 레이저가 나올때, 그 동안 여는괄호가 나온 만큼 스택에 추가 됩니다. 
       두 번째, 레이저가 아닐 경우에 닫는괄호가 나오면 결과값에 1개를 카운팅 해줘야 합니다.
       
        for i in range(len(ir)):
            if ir[i] == "(":
                stack.append("(")
            else :
                if ir[i-1]=="(":
                    stack.pop()
                    cnt+=len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.  
                else :
                    stack.pop()
                    cnt+=1 # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.

문제
https://www.acmicpc.net/problem/10799

입력
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

출력
잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.

예제 입력 1 
()(((()())(())()))(())
예제 출력 1 
17

예제 입력 2 
(((()(()()))(())()))(()())
예제 출력 2 
24

'''

import sys
input=sys.stdin.readline

total=list(input().rstrip())
stack=[]
piece=0
#print(total)
for i in range(len(total)):
    if total[i]=='(':
        if total[i+1]==')': # 레이저 
            piece+=len(stack)
        else:
            stack.append('(')
    elif total[i-1]!='(':
        stack.pop()
        piece+=1
    
    #print(stack,i, piece)

print(piece)

        
            
        

