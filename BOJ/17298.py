import sys
inp = sys.stdin.readline

if __name__ == "__main__":
    numbers = []
    result = []
    N = int(inp())
    numbers = list(map(int, inp().split()))

    for i, number in enumerate(numbers):
        for j in range(i, N):
            if numbers[i] < numbers[j]:
                result.append(numbers[j])
                break
            elif j==N-1:
                result.append(-1)

    print(result)
