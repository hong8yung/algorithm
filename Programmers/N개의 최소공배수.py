def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    if a < b:
        a, b = b, a
    return a*b/gcd(a, b)

def solution(arr):
    while len(arr) != 1:
        result = []
        for i in range((len(arr)+1)//2):
            result.append(lcm(arr[i], arr[-1-i]))
        arr = result
    return int(arr[0])


arr = [[2, 6, 8, 14], [1, 2, 3]]

print(solution(arr[0]))
print(solution(arr[1]))

#case0: 168
#case1: 6
