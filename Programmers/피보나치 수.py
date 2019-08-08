def solution_(n):
    sqrt_5 = 5 **(1/2)
    ans = 1/sqrt_5*( ((1+sqrt_5)/2)**n-((1-sqrt_5)/2)**n)
    return int(ans)%1234567


def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

n = [1, 2]
print(solution1(n[0]))
print(solution1(n[1]))