'''
21608번 상어 초등학교 골드5

>> 자리배정 2차원 리스트를 만들고 체크(인접한곳: 친구수, 공백) 각각 체크해
   우선순위에 따라서 배정하고 풀면 생각하는게 조금더 간단함
   내방법: 딕셔너리로 학생의 좌표를 기억, 각 좌표마다 인접한 칸의 개수 저장
   --> 120ms 빠르기는한데 너무 복잡하다는 생각이 든다. 
   그리고 첫번째 학생은 무조건 2,2 좌표에 배치된다는 규칙이 있다. 생각했다면 조금더 수월했을것 

문제
https://www.acmicpc.net/problem/21608

입력
첫째 줄에 N이 주어진다. 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.

학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수이다. 어떤 학생이 자기 자신을 좋아하는 경우는 없다.

출력
첫째 줄에 학생의 만족도의 총 합을 출력한다.

제한
3 ≤ N ≤ 20

예제 입력 1 
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
예제 출력 1 
54

예제 입력 2 
3
4 2 5 1 7
2 1 9 4 5
5 8 1 4 3
1 2 9 3 4
7 2 3 4 8
9 8 4 5 7
6 5 2 3 4
8 4 9 2 1
3 9 2 1 4
예제 출력 2 
1053

반례 
[Input]
3
1 2 3 4 5
2 3 4 5 6
3 1 4 5 6
4 5 6 7 8
5 1 3 4 6
6 4 5 7 8
7 1 2 8 9
8 3 4 7 9
9 5 6 7 8

[Output]
144

'''
import sys
from collections import defaultdict
input=sys.stdin.readline

def getSeat(y,x):
    temp=[]
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 1<=ny<=N and 1<=nx<=N and (ny,nx) not in seat.values():
           temp.append((ny,nx))
    return temp

# 자리 크기 
N= int(input())
like=defaultdict(int)
seat=defaultdict(int)


for _ in range(N*N):
    line=list(map(int,input().split()))
    like[line[0]]=line[1:]

dx,dy=[0,0,-1,1],[1,-1,0,0]
near_empty=defaultdict(int)

# 초기 인접 자리 값 구하기
for i in range(1,N+1):
    for j in range(1,N+1):
        near_empty[(i,j)]=len(getSeat(i,j))

for st,li in like.items():
    # 좋아하는 학생 인접칸 구하기 2,5,1,7 이 있는 칸 구하기
    temp_seat=defaultdict(int)
    ln=list(near_empty.items())
    
    for l in li:
        if seat[l]!=0:
            ts= getSeat(seat[l][0],seat[l][1])
            for t in ts:
                temp_seat[t]+=1
  
    if len(temp_seat)>0:
        
            k=max(temp_seat,key=lambda x:temp_seat[x])
           
            if list(temp_seat.values()).count(temp_seat[k])==1:
                ns=getSeat(k[0],k[1])
                del near_empty[k]
                for n in ns:
                    near_empty[n]-=1
                seat[st]=k
        
                continue
            
            ln=[]
            for ts in temp_seat:
                if temp_seat[k]==temp_seat[ts]:
                    ln.append((ts,near_empty[ts]))
              
            
    # 인접한 칸 중에서 비어있는 칸 가장 많은칸 자리
    # ((r,c),val)
    ln.sort(key=lambda x:(-x[1],x[0][0],x[0][1]))
    ns=getSeat(ln[0][0][0],ln[0][0][1])
    
    del near_empty[ln[0][0]]
    for n in ns:
        near_empty[n]-=1
    
    seat[st]=ln[0][0]
 
print(seat)
ans=0

for st,li in like.items():
    y,x=seat[st]
    score=0
    for l in li:
        if abs(y-seat[l][0])+abs(x-seat[l][1])==1:
            score+=1
    if score!=0:
        ans+=10**(score-1)

print(ans)
