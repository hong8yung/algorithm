from collections import deque
from sys import stdin
inp = stdin.readline

N = 0
matrix = []
check_mat = []
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
result = 0

def BFS(i, j, colorCh, dysch_flag):
    q = deque()
    q.append((i, j))
    check_mat[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if (nx<0 or nx>=N or ny<0 or ny>=N) or check_mat[nx][ny]:
                continue
            if dysch_flag is True:
                if colorCh == 'B' and (matrix[nx][ny] == 'R' or matrix[nx][ny] == 'G'):
                    continue
                if colorCh != 'B' and matrix[nx][ny] == 'B':
                    continue
            elif dysch_flag is False and matrix[nx][ny] != colorCh:
                continue

            q.append((nx, ny))
            check_mat[nx][ny] = True

def init():
    global result, check_mat
    result = 0
    check_mat = [[False]*N for _ in range(N)]

if __name__ == "__main__":
    N = int(inp())
    matrix = [list(inp().strip()) for _ in range(N)]
    init()

    for i in range(N):
        for j in range(N):
            if check_mat[i][j] is False:
                BFS(i, j, matrix[i][j], False)
                result += 1
    
    print(result, end=' ')

    init()

    for i in range(N):
        for j in range(N):
            if check_mat[i][j] is False:
                BFS(i, j, matrix[i][j], True)
                result += 1

    print(result)
