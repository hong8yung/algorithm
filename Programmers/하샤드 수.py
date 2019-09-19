def solution(x):
    tmp_sum = 0
    for i in str(x):
        tmp_sum += int(i)

    return x%tmp_sum==0

arr = [10, 12, 11, 13]
print(solution(arr[0]))
print(solution(arr[1]))
print(solution(arr[2]))
print(solution(arr[3]))