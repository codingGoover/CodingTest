'''
고득점 KIT 해시 전화번호 목록 Lv2

startwith라는 문자열 함수
print("dfagd".startswith("abcd"))
print("abcde".startswith("abcd"))
### False
### True

'''

# 내풀이를 더 잘푼 경우.. 해시맵 정석 이렇게 생각하면 참 좋을텐데 왜 못하지!!
def solution(phone_book): 

    # 1.Hash map생성
    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        arr = "" 
        for num in nums:    #문자 하나씩 더해감 
            arr += num
    
            # 3. 본인 자체일 경우는 제외
            if arr in hash_map and arr != nums:       
                return False 
                
    return True

# 내풀이. 길이마다 있는지 없는지를 체크하는 간단한 방식인데 예외 처리할 필요가 있는 케이스가 있었다.

from collections import defaultdict
def solution(phone_book):
    answer = True
    nlen=set()
    num=defaultdict(int)
    for p in phone_book:
        nlen.add(len(p))
        num[p]+=1
        
    prefix=defaultdict(int)
    #print(nlen)
    

    for p in phone_book:
        for l in nlen:
            if len(p)<l or num[p[:l]]==0:   #길이고려 추가해주니까 테스트11,14만 실패
            #모르겠어서 반례검색 존재하지 않는 번호가 접미사인 경우 를 놓쳤음
            # 예)  ["123", "2345", "23467"]  True인데 False출력
                continue
            
            if prefix[p[:l]]>0:
                return False
            else:
                prefix[p[:l]]+=1
            
    
    return True

# 찾아본 풀이. 정렬후 탐색
# 만약에 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치하게 된다.
# 예를 들어 ["1235", "123", "12348", "012"]을 입력으로 받으면, sorted(["1235", "123", "12348", "012"])는 ["012", "123", "12348", "1235"]가 된다.

# 따라서 phone_book을 정렬하고 for문을 이용해 phone_book[i]과 phone_book[i+1] 값을 비교했다.

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer


def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


