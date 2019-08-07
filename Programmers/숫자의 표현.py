def foo(cu_n, n, sum):
    if sum+cu_n < n and cu_n > 0:
        return foo(cu_n-1, n, sum+cu_n)
    elif sum+cu_n == n:
        return True
    else:
        return False

def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        if foo(i, n, 0):
            answer += 1

    return answer

#https://programmers.co.kr/learn/courses/30/lessons/12924/solution_groups?language=python3
def idel_sol(n):
    return len([i for i in range(1, n+1, 2) if n%i is 0])

n = 15
print(solution(n))