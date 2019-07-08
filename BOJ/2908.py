import sys
inp = sys.stdin.readline

if __name__ == "__main__":
    first, second = map(str, inp().split())
    first = int(first[::-1])
    second = int(second[::-1])

    print(max(first, second))