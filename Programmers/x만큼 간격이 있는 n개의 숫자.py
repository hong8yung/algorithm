def solution(x, n):
    return [x*(i+1) for i in range(n)]

def idle_solution(x, n):
    return list(range(x, x*n+1, x))

x = [2, 4, -4]
n = [5, 3, 2]

print(solution(x[0], n[0]))
print(solution(x[1], n[1]))
print(solution(x[2], n[2]))

print(idle_solution(x[0], n[0]))
print(idle_solution(x[1], n[1]))
print(idle_solution(x[2], n[2]))