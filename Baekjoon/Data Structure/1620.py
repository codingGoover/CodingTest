'''
1620번 나는야 포켓몬 마스터 이다솜 실버4

insight
    >> 문제설명만 길고 어이없는 문제 그냥 딕셔너리 쓰면됨
       
문제
https://www.acmicpc.net/problem/1620

예제 입력 1 
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

예제 출력 1 
Pikachu
26
Venusaur
16
14

'''
import sys
input=sys.stdin.readline

N,M= map(int,input().split())
dogam= dict()

for i in range(1,N+1):
    name=input().rstrip()
    dogam[name]=str(i)
    dogam[str(i)]=name

for _ in range(M):
    q= input().rstrip()
    print(dogam[q])
