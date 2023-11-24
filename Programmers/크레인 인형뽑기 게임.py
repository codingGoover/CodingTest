"""
크레인 인형뽑기 게임 Lv1

>> 스택 친숙해지기

"""
def solution(board, moves):
    answer = 0
    basket = []
    N = len(board)

    for m in moves:
        for i in range(N):
            if board[i][m - 1] != 0:
                basket.append(board[i][m - 1])
                board[i][m - 1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        answer += 2
                        basket.pop()
                        basket.pop()
                break

        # print(basket)

    return answer