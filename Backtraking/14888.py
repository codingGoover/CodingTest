'''
14888번 연산자 끼워넣기 실버1

insight 
    >>  삽질대마왕 백트래킹 1824ms
        "나눗셈은 정수 나눗셈으로 몫만 취하며, 
        음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 
        그 몫을 음수로 바꾼 것과 같다는 점"

        --> 안해줘서 계속 틀렸음
            파이썬:  -2//3 = -1  0이 아니라 -1로 뜸
            # int(total / num[depth]) 나누어주고 int로 묶어도됨 
        
        연산결과 값 전부 저장하지 않고 
        maximum, minimum 변수로 저장하면 시간 단축  --> 별차이 X  16ms ↓ 
        
문제
https://www.acmicpc.net/problem/14888


// input
2
5 6
0 0 1 0
=
3
3 4 5
1 0 1 0
=
6
1 2 3 4 5 6
2 1 1 1
=
2
1 2
1 0 0 0
=
5
1 2 3 4 5
1 1 1 1
=
5
100 100 100 100 10
0 0 4 0
=
11
1 2 3 4 5 6 7 8 9 10 11
10 0 0 0
=
6
1 2 3 4 5 6
5 0 0 0
=
2
-9 3
0 0 0 1

//output
1)
30
30

2)
35
17

3)
54
-24

4)
3
3

5)
20
-15

6)
1000000000
1000000000

7)
66
66

8)
21
21

9)
-3
-3

'''

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(cnt,v1,n):
   
    prev=-1
    #global p
    global maximum,minimum
    
    if cnt==N:
        #print(expression, p)
        #p+=1
        answer.append(v1)
        #maximum=max(v1,maximum)
        #minimum=min(v1,minimum)
        return
    
    for i in range (n+1,N):
        #print('n:%d'%number[i])
        for j,op in enumerate(ovisit):
            
            for l,visit in enumerate(op):
    
                if not visit and prev!=j:
                    if j==0:
                        v2=v1+number[i]
                    elif j==1:
                        v2=v1-number[i]
                    elif j==2:
                        v2=v1*number[i]
                    else:
                        v2=abs(v1)//number[i]
                        if v1<0:
                            v2=-v2
                        #v2=int(v1/number[i])

                    ovisit[j][l]=True
                    prev=j
                               
                    #expression.append(j)
                    dfs(cnt+1,v2,i)
                    ovisit[j][l]=False
                    #expression.pop()
                            
    
# 숫자의 개수 N
N= int(input())
number= list(map(int,input().split()))
# + - x /
op=list(map(int,input().split()))

ovisit=[[False for _ in range(op[i])] for i in range(4)]

#maximum=-1e9
#minimum=1e9

answer=[]

#p=0
#expression=[]
dfs(1,number[0],0)

#print(answer)

print(max(answer))
print(min(answer))

#print(int(maximum))
#print(int(minimum))


'''
 확실히 빠른 코드 60ms (1/3 수준)
        def dfs(depth, total, plus, minus, multiply, divide):
            global maximum, minimum
            if depth == N:
                maximum = max(total, maximum)
                minimum = min(total, minimum)
                return

            if plus:
                dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
            if minus:
                dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
            if multiply:
                dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
            if divide:
                dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

'''