'''
1987번 알파벳 골드4

insight
    >> DFS + 백트래킹
       시간초과에 빡빡한 문제
       visited[][] 이차원 배열이 언제 필요한지 생각하고 만들어서 써야함
       이문제는 alphabet의 유무 체크가 방문 체크와 동일한 의미 
       따로 필요없음! 그냥 별 생각없이 만들지 말것 이걸로 시간초과뜸 pypy3로 해야함

문제
https://www.acmicpc.net/problem/1987

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1 
2 4
CAAB
ADCB
예제 출력 1 
3

예제 입력 2 
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2 
6

예제 입력 3 
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
예제 출력 3 
10

예제 입력 4
20 20
ABCDEFGHIJKLMNOPQRST
BCDEFGHIJKLMNOPQRSTU
CDEFGHIJKLMNOPQRSTUV
DEFGHIJKLMNOPQRSTUVW
EFGHIJKLMNOPQRSTUVWX
FGHIJKLMNOPQRSTUVWXY
GHIJKLMNOPQRSTUVWXYY
HIJKLMNOPQRSTUVWXYYZ
IJKLMNOPQRSTUVWXYYZZ
JKLMNOPQRSTUVWXYYZZZ
KLMNOPQRSTUVWXYYZZZZ
LMNOPQRSTUVWXYYZZZZZ
MNOPQRSTUVWXYYZZZZZZ
NOPQRSTUVWXYYZZZZZZZ
OPQRSTUVWXYYZZZZZZZZ
PQRSTUVWXYYZZZZZZZZZ
QRSTUVWXYYZZZZZZZZZZ
RSTUVWXYYZZZZZZZZZZZ
STUVWXYYZZZZZZZZZZZZ
TUVWXYYZZZZZZZZZZZZZ
예제 출력4
26

'''
import sys
input=sys.stdin.readline

def dfs(x,y,len):
    global maxlen
    
    if maxlen<len:
        maxlen=len  

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<C and 0<=ny<R and graph[ny][nx] not in alphabet:     
                alphabet.add(graph[ny][nx])
                dfs(nx,ny,len+1)
                # 백트래킹
                alphabet.remove(graph[ny][nx])


#세로R 가로C
R,C= map(int,input().split())
graph=[list(input().rstrip()) for _ in range(R)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

maxlen=0
alphabet={graph[0][0]}
dfs(0,0,1)

print(maxlen)

