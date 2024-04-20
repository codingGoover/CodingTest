'''
Lv2 H-Index 
문제 이해를 못하면 너무 어렵게 느껴짐
처음에 반으로 나누면 될거같다는 이상한 접근으로 가서
우수수 틀리는것을 보았음.

혼자서 야매로 생각하는 접근 금지..
 
'''

# 테케9만 안돌아가는거 질문하기로 찾았다. 예제2 : [3, 4] >> 출력값 : 2
# 처음에 문제접근을 완전 잘못함 반정도 부터 검사하는게아니라. <- 말도안됨
# 그냥 0부터 다 차근차근 올라 갔어야함. 테케9도 그런원리. 괜히 시간줄여보겠다고. 정확도 터무니 없이 떨어뜨리는 접근을 하지 말자

def solution(citations):
    
    citations.sort()
    maxh= 0
    
    for h in range(0,citations[-1]+1):
        cnt=0
        
        for cidx,c in enumerate(citations):
            if c>=h:
                cnt=len(citations)-cidx
                break

        if cnt>=h:
            #print(h,maxh)
            maxh=max(h,maxh)
        else:
            break
            
    return maxh


# H-index 풀이를 찾아봄 오름차순 방식
def solution(citations):
    citations.sort()
    for idx , citation in enumerate(citations):
        if citation >= len(citations) - idx :
            return len(citations) - idx
    return 0

# 요약하자면 가장 많이 인용된 논문순으로 정렬한 후 피 인용수가 논문수와 같아지거나 작아지기 시작하는 숫자가 H-Index라는 것이다.
# 내림차순 방식
def solution(citations):
    answer = 0
    citations.sort(reverse = True) # 내림차순으로 정렬
    for num, citation in enumerate(citations):
        # 피 인용수가 논문의 수랑 같아지는 지점(num은 0부터 시작하니까 +1)
        if citation >= num+1: 
            h_index = num+1
            answer = h_index

    return answer