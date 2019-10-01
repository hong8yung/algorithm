def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer

def idle_solution(n):
    return sum(map(int, list(str(n))))

N = [123, 987]

print(solution(N[0]))
print(solution(N[1]))

print(idle_solution(N[0]))
print(idle_solution(N[1]))