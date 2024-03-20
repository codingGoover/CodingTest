'''
7568번 덩치 실버5

insight
>> 8879번이랑 유사 문제 , 조건에 따라서 자신보다 더 큰 덩치의 사람이 k명 을 구하면됨

 이름	(몸무게, 키)	덩치 등수
    A	(55, 185)	    2
    B	(58, 183)	    2
    C	(88, 186)	    1
    D	(60, 175)	    2
    E	(46, 155)	    5


입력
첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

출력
여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.

제한
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200

예제 입력 1 
5
55 185
58 183
88 186
60 175
46 155
예제 출력 1 
2 2 1 2 5

'''
import sys
input= sys.stdin.readline

N= int(input())
ans=[]
info=[list(map(int,input().split()))for _ in range(N)]

for i in range(N):
    up=0
    for j in range(N):
        if i!=j and info[j][0]> info[i][0] and info[j][1] > info[i][1]:
            up+=1
    ans.append(up+1)

print(*ans)