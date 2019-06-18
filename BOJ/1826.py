import sys
inp = sys.stdin.readline

def greedy():
    arr  = []
    queGS = []
    result = 0
    idx = 0

    for i in range(int(inp())):
        dstGS, volFuel = map(int, inp().split())
        arr.append((dstGS, volFuel))

    dstVlg, orgnlFuel = map(int, inp().split())
    arr = sorted(arr)

    while dstVlg > orgnlFuel:
        for i in range(idx, len(arr)):
            if (orgnlFuel >= arr[i][0]):
                queGS.append((arr[i][1]))
                idx = i+1;           
                print("orgnlFuel:{}, turn:{} // [+][stack psuhed] idx:{} -> que:{}".format(orgnlFuel, arr[i], idx, queGS))
            else:
                break
        
        if(len(queGS) == 0):
            return -1
        else:
            result += 1
            queGS = sorted(queGS)
            orgnlFuel += (queGS.pop())
            print("orgnlFuel:{}, turn:{} //[-][stack poped] idx:{} -> que:{}".format(orgnlFuel, arr[i],idx, queGS))
#        print("orgnlFuel:{} idx:{} -> que:{}".format(orgnlFuel, idx, queGS))


    return result

if __name__ == "__main__":
    print(greedy())
