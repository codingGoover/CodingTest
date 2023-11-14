"""
2007. 패턴 마디의 길이 D2

MMMMMMMMMOMMMMMMMMMOMMMMMMMMMO  --> MMMMMMMMMO
KOKOKKOKOKKOKOKKOKOKKOKOKKOKOK  --> KOKOK
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA  --> SAMSUNG

"""
import sys
sys.stdin= open("../input.txt","r")

T= int(input())

for t in range(1,T+1):
    string= str(input())

    # 열글자까지 체크
    for i in range(1,11):
        word= string[:i]
        flag=True
        for s in range(i,30-i+1,i):
            ch= string[s:s+i]
            if word!=ch:
                #print("%s %s"%(word, ch))
                flag=False
                break

        if flag:
            print("#%d %d"%(t,i))
            break