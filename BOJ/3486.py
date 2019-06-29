import sys
inp = sys.stdin.readline

def greedy():
    N = int(inp())
    for i in range(N):
        first, second = map(str, inp().split())
        sum = int(first[::-1]) + int(second[::-1])
        sum = int((str(sum)[::-1]))

        print(sum)

if __name__ == "__main__":
    greedy()