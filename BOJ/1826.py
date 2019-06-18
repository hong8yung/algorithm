import sys
inp = sys.stdin.readline

def greedy():
    arr  = []
    queGS = []
    result = 0

    for i in range(int(inp())):
        dstGS, volFuel = map(int, inp().split())
        arr.append((dstGS, volFuel))

    dstVlg, orgnlFuel = map(int, inp().split())
    arr = sorted(arr)

    while orgnlFuel < dstVlg:
        for GS in arr:
            if GS[0] > orgnlFuel:
                break
            else:
                queGS.append(GS[1])
        if len(queGS)==0: 
            break
        result += 1
        orgnlFuel += queGS.pop()

    if orgnlFuel < dstVlg: return -1
    else: return result

if __name__ == "__main__":
    print(greedy())
