"""
2056. 연월일 달력 D1
>> string 을 int로 잘 변환하자

"""

import sys
sys.stdin=open("../input.txt","r")
input=sys.stdin.readline

last=[31,28,31,30,31,30,31,31,30,31,30,31]
T = int(input())
for test_case in range(1, T + 1):

    string= str(input())
    year=string[:4]
    month=string[4:6]
    day=string[6:8]

    if 1<=int(month)<=12 and 1<=int(day)<=last[int(month)-1]:
        print("#%d %s" %(test_case,year+'/'+month+'/'+day))
    else:
        print("#%d %d" %(test_case,-1))


