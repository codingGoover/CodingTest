'''
2021 Dev-Matching: 웹 백엔드 개발자(상반기) 
Lv1 로또의 최고 순위와 최저 순위
>> 똑바로 문제읽기
'''
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt=0
    x=0
    
    for l in lottos: 
        if l==0:
            x+=1
        if l in win_nums:
            cnt+=1

    answer=[rank[cnt+x],rank[cnt]]
    
    return answer