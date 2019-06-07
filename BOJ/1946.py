import sys
inp = sys.stdin.readline

T = int(inp())
dict = {}
for i in range(T):
    N = int(inp())
    dict.clear

    for j in range(N):
        a, b = inp().split()
        dict[int(a)] = int(b)

    sortedArr = sorted(dict.items())
    min = 100001
    res = 0

    for j in sortedArr:
        if(min > j[1]):
            min = j[1]
            res += 1 
   
    print(res)