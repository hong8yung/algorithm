def solution(board):
    answer = 0
    if 2 > len(board) or 2 > len(board[0]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    return 1
            
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
                answer = max(answer, board[i][j])
    else:
        return answer ** 2


board = [
	[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]],
	[[0,0,1,1],[1,1,1,1]]
	]

print(solution(board[0]))
print(solution(board[1]))

