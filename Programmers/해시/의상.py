'''
고득점 KIT 해시 의상 Lv2

경우의 수를 곱으로 구하는 문제였다. 
(옷개수+1) * (옷개수+1) * .. - 1  <- 아무것도 안입는 경우
간단한 경우의 수인데 나오는 가지수를 서로 곱한다는 생각을 못했다. 

'''


def solution(clothes):
    kind=dict()
    
    for n,k in clothes:
        if kind.get(k,-1)==-1:
            kind[k]=1
        else:
            kind[k]+=1
    
    answer=1
    #print(kind)
    for count in kind.values():
        answer *= count+1
    
    
    return answer -1