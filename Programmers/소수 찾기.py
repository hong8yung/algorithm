import math

def solution(n):
    tmp = [True] * (n+1)
    for i in range(2, int(math.sqrt(n)+1)):
        if(tmp[i]):
            for j in range(i*2, n+1, i):
                tmp[j] = False
    
    return tmp.count(True) - 2

def solution_idle(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))

    return len(num)

n = [20, 29]
print(solution(n[0]))
print(solution(n[1]))