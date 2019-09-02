def solution(n):
    tmp = [1,2]
    for i in range(2, n):
        tmp.append(tmp[i-2] + tmp[i-1])

    return tmp[n-1]%1234567

n = [1, 3]

print(solution(n[0]))
print(solution(n[1]))
