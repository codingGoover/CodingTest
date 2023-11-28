'''
[PCCP 모의고사 #2] 1번 - 실습용 로봇 Lv1

>> 방향을 인덱스로 설정하고 전진/후진에 따라 + , - 
   아이디어 문제
'''

DIR=[(0,1),(1,0),(0,-1),(-1,0)]
def solution(command):
    x,y,i=0,0,0
    
    for c in command:
        if c=='R':
            i=(i+1)%4
        elif c=='L':
            i=(i-1)%4  # (0-1) %4 = 3  -->  -1 = -1 * 4 + 3
        elif c=='G':
            #dx,dy=DIR[i]
            x+=DIR[i][0]
            y+=DIR[i][1]
        elif c=='B':
            #dx,dy=DIR[i]
            x-=DIR[i][0]
            y-=DIR[i][1]
    
    return [x,y]
