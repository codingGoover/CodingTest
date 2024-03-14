'''
8
2
4
7
5
3
1
8
6
'''

import sys
input=sys.stdin.readline



stack= []
sequence=[]
ans=[]
n= int(input())
cur=1

for _ in range(n):
    sequence.append(int(input()))

#print(sequence)

for s in sequence:
    
    # 스택 push 가능한 숫자가 있는 경우
    if cur<=n:    
        while cur<=s:
            stack.append(cur)
            ans.append('+')
            cur+=1
    
    if s<stack[-1]:
        print('NO')
        print(*ans,sep='\n')
        sys.exit()
    
    if s==stack[-1]:
        ans.append('-')
        stack.pop()
    
           
print(*ans,sep='\n')



