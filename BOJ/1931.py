import sys
inp = sys.stdin.readline

def greedy():
    num = int(inp())
    cnfrArr = []

    for i in range(num):
        start, end = map(int, inp().split())
        cnfrArr.append((start, end))       

    cnfrArr = sorted(cnfrArr, key=lambda tmp: tmp[0])
    cnfrArr = sorted(cnfrArr, key=lambda tmp: tmp[1])
    current = 0
    result = 0

    for (start, end) in cnfrArr:
        if(start >= current):
            current = end
            result += 1

    return result

if __name__ == "__main__":
    print(greedy())