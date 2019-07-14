from sys import stdin
inp = stdin.readline

if __name__=="__main__":
    A_arr, B_arr = [], []
    N = int(inp())

    A_arr = list(map(int, inp().split()))
    B_arr = list(map(int, inp().split()))

    A_arr.sort()
    answer = 0
    for i in range(N):
        answer += A_arr[i] * max(B_arr)
        B_arr.remove(max(B_arr))

    print(answer)