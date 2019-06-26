import sys
inp = sys.stdin.readline

def greedy():
    diffCnt = 0
    sample = inp()

    if sample[0] == '0':
        zero += 1
    else : one += 1

    for i in range(1, len(sample)):
        if sample[i] != sample[i-1]:
            diffCnt += 1

    return int(diffCnt/2)
if __name__ == "__main__":
    print(greedy())