import sys
inp = sys.stdin.readline

def greedy():
    num = int(inp())
    numList = list(map(int, input().split()))
    result = []

    for i in range(num-1, -1, -1):
        result.insert(numList[i], i+1)
    
    for i in result:
        print(i, end=' ')
if __name__ == "__main__":
    greedy()