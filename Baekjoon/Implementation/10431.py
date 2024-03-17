'''
10431번 줄세우기 실버5

애들을 정렬할 건데 버블 정렬로 정렬해서 몇번 정렬을 하면 끝나니? 
를 묻고 있는 문제

버블정렬?

def Bubblesort(List): #정렬할 list, 원소 수 N
    global cnt
    for i in range(len(List)-1, 0, -1) : # 범위의 끝
        for j in range(i) :
            if List[j] > List[j+1] : #현재 항이 다음 항보다 클 경우
                List[j], List[j+1] = List[j+1], List[j] #서로의 위치를 바꿔라
                cnt += 1

T = int(input())
for _ in range(T):
    N, *x = map(int,input().split())
    cnt = 0
    Bubblesort(x)
    print(N, cnt)
 
'''

import sys
input=sys.stdin.readline

P= int(input())
for i in range(1,P+1):
    student=list(map(int,input().split()))
    cnt=0
    sort_h=[student[1]]
    for j in range(2,21):
        for s in sort_h:
            if s>student[j]:
                cnt+=1
        sort_h.append(student[j])
    
    print(f'{i} {cnt}')

    