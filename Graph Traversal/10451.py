'''
10451번 순열사이클 실버3

문제
https://www.acmicpc.net/problem/10451

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

예제 입력 1 
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8

예제 출력 1 
3
7

예제 입력 2
6
3
1 2 3
3
3 2 1
3
2 1 3
3
3 1 2
3
1 3 2
3
2 3 1

예제 출력 2
3
2
2
1
2
1

insight
>> 순열의 특성상 한 숫자가 반복등장이 불가능하므로 어떤 경우든 사이클이 형성되는 것을 알게됨

'''

from collections import deque
import sys
input=sys.stdin.readline

def bfs(graph,visted,node):
    global cycle
    
    visted[node]=True
    now_node=node
    
    while True:
        visted[now_node]=True
        now_node=graph[now_node]
        if now_node==node:
            cycle+=1
            break
        if visted[now_node]==True:
            break
    
    
N= int(input())
for _ in range(N):
    cnt= int(input())
    cycle=0
    visted=[False]*(cnt+1)
    graph=[0]
    
    graph.extend(map(int,input().split()))
    #print(graph)
    
    for i in range(1,cnt+1):
        if visted[i]==False:
            if graph[i]==i:
                cycle+=1
                visted[i]=True
            else:
                bfs(graph,visted,i)
    
    print(cycle)
    
                
    
