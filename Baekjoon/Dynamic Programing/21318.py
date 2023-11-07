'''
21318번 피아노 체조 실버1

문제
https://www.acmicpc.net/problem/21318

insight
    >> 하나씩 비교해서 실수한 연주를 누적합으로 저장해야함 (칠윤아이디어,,,)
       O(N) 한번으로 끝낼 수 있도록 시간제한 0.5초
       누적합 문제는 0번 인덱스를 마진값 0으로 두는게 편하다. 

입력
첫 번째 줄에 악보의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.

두 번째 줄에 1번 악보부터 N번 악보까지의 난이도가 공백을 구분으로 주어진다.

세 번째 줄에 질문의 개수 Q(1 ≤ Q ≤ 100,000)이 주어진다.

다음 Q개의 줄에 각 줄마다 두 개의 정수 x, y(1 ≤ x ≤ y ≤ N)가 주어진다.

출력
x번부터 y번까지의 악보를 순서대로 연주할 때, 몇 개의 악보에서 실수하게 될지 0 이상의 정수 하나로 출력한다. 각 출력은 개행으로 구분한다.

예제 입력 1 
9
1 2 3 3 4 1 10 8 1
5
1 3
2 5
4 7
9 9
5 9
예제 출력 1 
0
0
1
0
3

'''
import sys
input= sys.stdin.readline
# 악보 개수
N= int(input())
psum=[0]*(N+1)
sheet=list(map(int,input().split()))

for i in range(N-1):
    if sheet[i]>sheet[i+1]:
        psum[i+1]=psum[i]+1
    else:
        psum[i+1]=psum[i]

#print(psum)
# 질문 개수
Q= int(input())
for _ in range(Q):
    x,y= map(int,input().split()) # 악보 범위 x<=y
    # 마지막 연주 y번에서는 절대 실수를 하지 않는다 --> psum[y]를 볼필요 x 이전값 봐야함
    ssum=psum[y-1]-psum[x-1]
    print(ssum)