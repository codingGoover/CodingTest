"""
1206. [S/W 문제해결 기본] 1일차 - View D3

양옆으로 연속 두개의 빌딩 높이 비교해
조망권을 확보되었는지 체크하는 문제

"""
import sys
sys.stdin= open("../input.txt","r")

for t in range(1,11):
    # 건물 개수 N
    N= int(input())
    building=list(map(int,input().split()))
    cnt=0
    for i in range(2,N-2):
        left=max(building[i-2:i])
        right=max(building[i+1:i+3])
        #print(left,right)
        if building[i]> max(right,left):
            cnt+=building[i]-max(right,left)

    print(f'#{t} {cnt}')