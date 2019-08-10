def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in zip(A,B):
        answer += i[0]*i[1]
    return answer

A = [[1,4,2], [1,2]]
B = [[5,4,4], [3,4]]

print(solution(A[0], B[0]))
print(solution(A[1], B[1]))