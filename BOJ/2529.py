import sys
inp = sys.stdin.readline

def greedy():
    num = int(inp())
    inqltArr = list(map(str, inp().split()))
    
    maxNumArr = []
    minNumArr = []
    for i in range(num+1):
        minNumArr.append(i)  
        maxNumArr.append(9-i)
    
    for i, inqlt in enumerate(inqltArr):
        if inqlt == '>':
            minNumArr[i], minNumArr[i+1] = minNumArr[i+1], minNumArr[i]
        else :
            maxNumArr[i], maxNumArr[i+1] = maxNumArr[i+1], maxNumArr[i]
    for i in maxNumArr:
        print(i, end="")

    print("")
    for i in minNumArr:
        print(i, end="")


if __name__ == "__main__":
    greedy()