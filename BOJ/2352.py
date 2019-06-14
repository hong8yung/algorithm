import sys
inp = sys.stdin.readline

def greedy():
    num = int(inp())
    minNum = 0
    arr = []
    res = 0
    tmp = list(map(int, inp().split()))

    for i, num_tmp in enumerate(tmp):
        i+=1
        if(i < num_tmp):
            arr.append((num_tmp, i))
        else :
            arr.append((i, num_tmp))
        
    arr = sorted(arr)

    for i in arr:
        if(i[1] > minNum):
            minNum = i[0]
            res+=1


    return res

if __name__ == "__main__":
    print(greedy())