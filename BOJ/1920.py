from sys import stdin
inp = stdin.readline

arr = []

def bisect(x, lo=0, hi=None):
    global arr
    if hi==None:
        hi = len(arr)

    while lo<hi:
        mid = (lo+hi) // 2
        if arr[mid] < x:
            lo = mid+1
        else:
            hi = mid
            
    return 1 if lo<len(arr) and arr[lo]==x else 0

if __name__ == "__main__":
    arr_size = int(inp())
    arr = list(map(int, inp().split()))

    size = int(inp())
    srch_arr = list(map(int, inp().split()))

    arr.sort()

    for i in range(size):
        print(bisect(srch_arr[i]))
