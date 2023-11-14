"""
1928 Base64 Decoder D2

인코드/디코드 원리 이해
https://ssanggo.tistory.com/36

format(42, 'b') --> '101010'  10진수를 2진수로 바꿔줌
int(string, base)  base에는 진법을 넣으면됨
int('101',2) --> 5
"""
import sys
sys.stdin= open("../input.txt","r")

T = int(input())

# 표 1
decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
          ]

for t in range(1,T+1):
    bit= input()
    result=""

    # 문자열을 문자 4개로 쪼개서 봄  TGlm
    for j in range(0,len(bit),4):
        temp=""
        # TGlm -> T G l m  -> (이진수)(이진수)(이진수)(이진수)
        for k in bit[j:j+4]:
            # 숫자를 이진수형태로 바꾸는데 6비트 형식을 맞춰줌 1 -> 000001
            temp+= format(decode.index(k),'b').zfill(6)
        # 24bit 이진수 배열을 8bit로 쪼갬 -> 문자1,문자2,문자3
        for m in range(0,len(temp),8):
            result+=chr(int(temp[m:m+8],2))

    print("#%d %s"%(t,result))


