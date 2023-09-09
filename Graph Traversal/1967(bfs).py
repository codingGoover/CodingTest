'''
1967번 트리의 지름 골드4

문제
https://www.acmicpc.net/problem/1967

insight
    >> 루트에서 가장 멀리 떨어진 노드 탐색
       그 노드에서 또 가장 멀리 떨어진 노드 탐색
       끝과 끝점을 알 수 있음
       함수는 리스트도 반환할 수있음. 코드를 줄일있수 있는 방법

       BFS 탐색 순서
       1 2 3 4 5 6 7 8 9 10 11 12
       9 5 3 10 1 6 2 11 12 4 7 8
       
입력
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1 
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
예제 출력 1 
45
'''
import sys
from collections import deque
input= sys.stdin.readline

def bfs(start):
    visted=[-1]*(N+1)
    queue= deque([start])
    visted[start]=0
    
    while queue:
        node=queue.popleft()
        print(node, end=' ')
        for (op,weight) in tree[node]:
            if visted[op]==-1:
                visted[op]=visted[node]+weight
                queue.append(op)
    m=max(visted)
    print()
    return [visted.index(m),m]

N= int(input())
tree=[[] for _ in range(N+1)]

#부모,자식,가중치
for _ in range(N-1):
    p,c,w= map(int,input().split())
    tree[p].append((c,w))
    tree[c].append((p,w))


print(bfs(bfs(1)[0])[1])