'''
자연수 뒤집어 배열로 만들기 Lv1

insight
    >> list(map(자료형,라스트))
    
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]4

'''
def solution(n):
    temp= list(str(n))
    answer= list(map(int,temp[::-1]))
    return answer


'''
A로 B만들기 Lv0

>> 굳이 순서 안바꾸고 정렬해서 같은 문자열인지 체크하면됨,,
   string 은 sort 가 안되어서 sorted 결과로 리스트를 반환함
   리스트끼리 비교한 격

문제 설명
문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

제한사항
0 < before의 길이 == after의 길이 < 1,000
before와 after는 모두 소문자로 이루어져 있습니다.

입출력 예
before	after	result
"olleh"	"hello"	1
"allpe"	"apple"	0

'''
def solution(before, after):
    answer=0
    
    if sorted(before)==sorted(after):
        answer=1
    
    return answer


'''
정수 내림차순으로 배치하기 Lv1

>> sorted(문자열,reverse=True)
   내림차순 정렬된 문자열이 리스트형으로 반환된다.
   sorted(리스트) <- 인자로 리스트가 들어갈수 있고 return 도 리스트다

문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.

입출력 예
n	return
118372	873211

'''
def solution(n):
    answer=int(''.join(sorted(str(n),reverse=True)))
    return answer