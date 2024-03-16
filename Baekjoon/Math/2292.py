'''
2292번 벌집 브론즈2

insight
    >> 수식 이런거 필요없고 그냥 그대로 구현하면됨,,
       6배로 늘어나는 숫자의 범위를 그대로 체크하면됨
       숫자 범위 >= 입력값 N이면 cnt출력
       number += 6*cnt
       cnt+=1

1 → 2~7 → 8~19 → 20~37 → 38~61 → 62~
1    6     12     18       24     30     

1+ 6( 0+ 1+ 2 +3 )

'''

import sys
input=sys.stdin.readline

N= int(input())
for r in range (0, N) :
    #print(r, (N-1))
    if (N-1) - r *(r+1) *3 <=0:
        print(r+1)
        break



N= int(input())
cnt=1
number=1

while N > number:
    number += cnt*6  # 벌집이 6의 배수로 증가
    cnt+=1           # 반복문을 반복하는 횟수

print(cnt)
