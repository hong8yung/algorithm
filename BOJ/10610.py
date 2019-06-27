import sys
inp = sys.stdin.readline

def greedy():
    inpStr = int(inp())
    result = []
    sumres = 0
    for i in str(inpStr):
        result.append(i)

    if '0' not in result:
        return -1

    for i in result:
        sumres += int(i)

    if sumres%3 != 0:
        return -1

    result.sort(reverse=True)
    return int("".join(result))
        
if __name__ == "__main__":
    print(greedy())
