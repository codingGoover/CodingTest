'''
구현 N개의 최소공배수 Lv1

최소공배수는 제일 큰 수의 배수로 알아가면 되는것
'''

def solution(arr):
    
    
    arr.sort()
    n=1
    ans=arr[-1]
    
    while True:
        flag=True
        
        for a in arr:
            if ans%a!=0:
                flag=False
                break
        
        if flag:
            break
        else:
            n+=1
            ans= arr[-1]*n
        
    return ans