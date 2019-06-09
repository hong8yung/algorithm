import sys
inp = sys.stdin.readline

def greedy():
    antArr = []
    barLen, antNum = map(int, inp().split()) 
    timeMin = timeMax = 0
    for i in range(antNum):
        antArr.append(int(inp()))

    for ant in antArr:
        timeMin = max(min(barLen-ant, ant), timeMin)
        timeMax = max(max(barLen-ant, ant), timeMax)

    print(timeMin, timeMax)
    
if __name__ == "__main__":
    caseNum = int(inp())
    for i in range(caseNum):
        greedy()