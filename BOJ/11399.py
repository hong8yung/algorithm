
import sys
inp = sys.stdin.readline

def greedy():
    timeArr = []
    result= tmp = 0
    num = int(inp())
    timeArr = inp().split()

    for i, e in enumerate(timeArr):
        timeArr[i] = int(e)

    timeArr = sorted(timeArr)
    for i in timeArr:
        tmp = tmp + i
        result += tmp 

    return result

if __name__ == "__main__":
    print(greedy())