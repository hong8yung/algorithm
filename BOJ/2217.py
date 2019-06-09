import sys
inp = sys.stdin.readline

def greedy():
    maxW = 0
    ropeNum = 0
    num = int(inp())
    ropeArr = []

    for i in range(num):
        ropeArr.append(int(inp()))

    ropeArr = sorted(ropeArr)
    ropeNum = len(ropeArr)

    for rope in ropeArr:
        maxW = max(maxW, rope * ropeNum)
        ropeNum -= 1

    return maxW

if __name__ == "__main__":
    print(greedy())