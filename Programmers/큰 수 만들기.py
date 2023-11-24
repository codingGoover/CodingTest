"""
큰 수 만들기 Lv2 그리디(Greedy)

>> stack을 활용하는 것이 포인트..
   그렇지 않으면 시간초과남 10번케이스에서 계속 났음
   등장할때 마다 숫자를 push

   뺄수있는 횟수 k가 더 남은 경우:
   등장하는 숫자보다 스택에 쌓여있는 수들이 작으면 pop

"""


def solution(number, k):
    answer = []

    for n in number:
        if len(answer) == 0:
            answer.append(n)
            continue
        if k > 0:
            while answer[-1] < n:
                answer.pop()
                k -= 1
                if len(answer) == 0 or k <= 0:
                    break

        answer.append(n)

    answer = answer[:-k] if k > 0 else answer

    return ''.join(answer)

# 원레 내 코드
def solution(number, k):
    answer = ''
    nlst = list(number)
    s = 0
    while k > 0:
        for i in range(s, len(nlst) - 1):
            if nlst[i] == '9':
                continue
            if nlst[i] < nlst[i + 1]:
                del nlst[i]
                k -= 1
                break
        # print(f'max:{max_n} i:{i} s:{s} {nlst}')
        s = max(0, i - 1)

        if i == len(nlst) - 2:
            break

    # "987654321" k=5 같은 경우 --> "9876"
    if k != 0:
        answer = ''.join(nlst[:-k])
    else:
        answer = ''.join(nlst)

    return answer