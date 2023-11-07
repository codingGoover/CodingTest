'''
1967번 트리의 지름 골드4

문제
https://www.acmicpc.net/problem/1967

DFS탐색 순서
1 2 4 7 8 3 5 9 10 6 11 12
9 5 3 1 2 4 7 8 6 11 12 10

'''

import sys

sys.setrecursionlimit(10 ** 6)
input= sys.stdin.readline
nodeCnt= int(input())

#노드개수+1 만큼 리스트를 리스트안에 
tree=[[] for _ in range(nodeCnt+1)]


#주어진 노드에서 시작해 해당노드까지 길이 구하기 위하여 깊이 우선 탐색
def dfs(node, weight):
    distance[node] = weight  
    for i in tree[node]:
        opNode, opWeight = i  #oppsite 
        if distance[opNode] == -1:  #방문하지 않은(거리를 찾지못한)노드라면
            dfs(opNode, weight + opWeight)


#간선 정보 받기 -> 트리 구성
for _ in range(nodeCnt-1):
    a,b,c= map(int,input().split())
    tree[a].append([b,c]) #연결노드,가중치 저장
    tree[b].append([a,c]) 

distance = [-1] * (nodeCnt + 1)  # 거리저장 리스트 
dfs(1, 0)  #루트노드에서 각 노드들 길이 탐색


#가장 먼 노드를 시작노드로 만들고 다시 dfs탐색 
start = distance.index(max(distance))  
distance=[-1]*(nodeCnt+1) 
dfs(start,0) 
maxDistance= max(distance)


print(maxDistance)