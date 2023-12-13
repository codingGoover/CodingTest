'''
20546번 🐜기적의 매매법🐜 실버5

>> 구현 바아아아보
'''
import sys
input=sys.stdin.readline

money=int(input())
stock=list(map(int,input().split()))

class Person:
    def __init__(self,cash):
        self.cash=cash
        self.asset=0
        self.cnt=0
    
    def getAsset(self):
        self.asset=self.cash+self.cnt*stock[13]
        
    def buy(self,st):
        self.cnt+=self.cash//st
        self.cash-=self.cash//st*st
        
    def sell(self,st):
        self.cash+=self.cnt*st
        self.cnt=0

jun=Person(money)
sung=Person(money)

for st in stock:
    if st<=jun.cash:
        jun.buy(st)

    if jun.cash==0:
        break


for i in range(3,14):
    # 성민이 돈도 있고 매수도 할 수 있음
    if sung.cash>=stock[i] and stock[i-3]>stock[i-2]>stock[i-1]>stock[i]:
        sung.buy(stock[i])
            
    # 성민이 사놓은 주식도 있고 매도도 할수 있음   
    elif sung.cnt>0 and i<11 and stock[i]<stock[i+1]<stock[i+2]<stock[i+3]:
        sung.sell(stock[i+3])

jun.getAsset()
sung.getAsset()

if jun.asset>sung.asset:
    print('BNP')
elif jun.asset<sung.asset:
    print('TIMING')
else:
    print('SAMESAME')


'''
처음에 생각한 방식과 비슷한 코드 더 간단?

import sys

input = sys.stdin.readline

n = int(input().rstrip()) #주어진 돈

chart = list(map(int, input().rstrip().split())) #주식 정보

BNP = [n, 0] #준현 돈, 주식 수
TIMING = [n, 0] #상민 돈, 주식 수

for i in range(len(chart)): #준현
    BNP[1] += (BNP[0] // chart[i]) #살 수 있는 만큼 사기 
    BNP[0] -= (BNP[0] // chart[i] * chart[i]) #주식 사고 남은 돈


for i in range(11): #성민
    check = chart[i:i+4]
    check_up = 0
    check_down = 0

    for j in range(3):
        if check[j+1] > check[j]: #상승 체크
            check_up+=1
        if check[j+1] < check[j]: #하락 체크
            check_down+=1

    if check_down == 3: #3일 연속 상승이면 전량매수
        TIMING[1] += (TIMING[0] // chart[i+3]) 
        TIMING[0] -= (TIMING[0] // chart[i+3] * chart[i+3])

    elif check_up == 3: #3일 연속 하락이면 전량매도
        TIMING[0] += (TIMING[1] * chart[i+3])
        TIMING[1] = 0

BNP = chart[13] * BNP[1] + BNP[0] #준현 총 금액
TIMING = chart[13] * TIMING[1] + TIMING[0] #성민 총 금액

if BNP>TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")
'''
