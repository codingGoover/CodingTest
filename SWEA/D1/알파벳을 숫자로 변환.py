"""
 2050. 알파벳을 숫자로 변환 D1
 >> ord(문자)  --> 아스키코드 숫자값으로 변환 A: 65
 >> chr(숫자)  --> 해당 아스키코드 숫자값을 문자로 변환  chr(65) : A
"""

import sys
sys.stdin= open("../input.txt","r")
input=sys.stdin.readline

alphabet= str(input())
for a in alphabet:
    print('%d' %(ord(a)-ord('A')+1), end=' ')
