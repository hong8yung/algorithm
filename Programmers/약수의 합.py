def solution(n):
    return sum([x for x in range(1, n+1) if n%x==0])

n = [12, 5]
print(solution(n[0]))
print(solution(n[1]))