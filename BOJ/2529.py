import sys
inp = sys.stdin.readline

def greedy():
    num = int(inp())
    inqltArr = inp().split()
    max_stack, min_stack = [], []
    
    maxNumArr = []
    minNumArr = []
    
    for idx in range(num+1):
        min_stack.append(str(idx))
        max_stack.append(str(9-idx))
        if idx == num:
            while len(max_stack)>0:
                maxNumArr.append(max_stack.pop())
            while len(min_stack)>0:
                minNumArr.append(min_stack.pop())
        elif inqltArr[idx]=='>':
            while len(max_stack)>0:
                maxNumArr.append(max_stack.pop())
        elif inqltArr[idx]=='<':
            while len(min_stack)>0:
                minNumArr.append(min_stack.pop())

    maxNum = "".join(maxNumArr)
    minNum = "".join(minNumArr)

    print(maxNum, minNum)

if __name__ == "__main__":
    greedy()