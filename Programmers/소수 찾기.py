import math

def solution(n):
    tmp = [True] * (n+1)
    for i in range(2, int(math.sqrt(n)+1)):
        if(tmp[i]):
            for j in range(i*2, n+1, i):
                tmp[j] = False
    
    return tmp.count(True) - 2

n = [20, 29]
print(solution(n[0]))
print(solution(n[1]))