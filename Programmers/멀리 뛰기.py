def solution(n):
    if n in (1, 2):
        return n
    return solution(n-1) + solution(n-2)

n = [4, 3]

print(solution(n[0]))
print(solution(n[1]))
