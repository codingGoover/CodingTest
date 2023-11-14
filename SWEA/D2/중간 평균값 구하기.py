"""
1984. 중간 평균값 구하기 D2

아예 최댓값과 최소값을 삭제함

"""
import sys
sys.stdin= open("../input.txt","r")

T= int(input())
for t in range(1,T+1):
    numbers=list(map(int,input().split()))
    numbers.remove(min(numbers))
    numbers.remove(max(numbers))

    print(f'#{t} {round(sum(numbers)/len(numbers))}')

