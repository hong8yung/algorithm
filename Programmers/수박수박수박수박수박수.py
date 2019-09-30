def solution(n):
    if n%2 == 0:
        return "수박" * (n//2)
    else:
        return "수박" * (n//2) + "수"

n = [3, 4]

print(solution(n[0]))
print(solution(n[1]))