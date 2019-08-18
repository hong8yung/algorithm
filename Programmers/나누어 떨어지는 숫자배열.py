def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)

    if not answer: answer.append(-1)
    else: answer.sort()

    return answer

# or 연산자로 하여금 sorted된 값이 빈 값 일때, 즉 False를 반환하므로 or연산자를 통해 [-1]리스트를 반환함...
def idle_solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]


arr = [[5,9,7,10], [2,36,1,3], [3,2,6]]
divisor = [5, 1, 10]

print(solution(arr[0], divisor[0]))
print(solution(arr[1], divisor[1]))
print(solution(arr[2], divisor[2]))