'''
20444번 색종이와 가위 골드5

문제
https://www.acmicpc.net/problem/20444

>> 이분 탐색으로 다시 만들어서 풀어볼것
 
입력
첫 줄에 정수 n, k가 주어진다. (1 ≤ n ≤ 231-1, 1 ≤ k ≤ 263-1)

출력
첫 줄에 정확히 n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력한다.

예제 입력 1 
4 9
예제 출력 1 
YES

예제 입력 2 
4 6
예제 출력 2 
NO

예제 입력 3
1 1
예제 출력 3
NO

예제 입력 4
100 100 
예제 출력 4
NO

'''
import sys
input=sys.stdin.readline

# n번 가위질 -> K개 색종이
N,K= map(int,input().split())


if N+1==K:
    print("YES")
    sys.exit()
if N+1>K:
    print("NO")
    sys.exit()

if K< (N//2+1)*(N-N//2+1)/2:
  for n in range(N//2+1):
    n2=N-n
    k=(1+n)*(1+n2)
    #print(n,n2,k)
    if k<K:
        continue
    elif k==K:
        print("YES")
        break
    elif k>K:
        print("NO")
        break
else:
    for n in range(N//2,-1,-1):
        n2=N-n
        k=(1+n)*(1+n2)
        #print(n,n2,k)
        if k==K:
            print("YES")
            break
        elif k<K:
            print("NO")
            break




    