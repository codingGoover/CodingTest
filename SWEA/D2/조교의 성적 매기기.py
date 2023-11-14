"""
1983. 조교의 성적 매기기 D2

입력 범위를 잘 보자
학생의 순서를 1번부터 부여함
idx+1 이 필요함

"""

import sys
sys.stdin= open("../input.txt","r")
grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
T= int(input())
for t in range(1,T+1):
    # 학생수 M  성적알고싶은 학생 K
    M,K= map(int,input().split())
    score=[list(map(int,input().split())) for _ in range(M)]
    student=[]
    for idx,sc in enumerate(score):
        sum_sc=sc[0]*0.35+ sc[1]*0.45 + sc[2]*0.2
        student.append((idx+1,sum_sc))

    student.sort(key=lambda x:x[1], reverse=True)

    for idx,st in enumerate(student):
        #print(idx, st)
        if st[0]==K:
            print("#%d %s"%(t,grade[idx//(M//10)]))
            break


