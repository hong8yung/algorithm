def solution(a, b):
    if a>b: a,b = b,a
    return sum(x for x in range(a, b+1))
     
a = [3,3,5]
b = [5,3,3]
print(solution(a[0], b[0]))
print(solution(a[1], b[1]))
print(solution(a[2], b[2]))