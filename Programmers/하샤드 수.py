def solution(x):
    tmp_sum = 0
    for i in str(x):
        tmp_sum += int(i)

    return x%tmp_sum==0

def row_solution(x):
    tmp_sum = 0
    tmp_num = x
    while tmp_num:
        tmp_sum += tmp_num%10
        tmp_num //= 10

    return x%tmp_sum is 0
    


arr = [10, 12, 11, 13]
print(solution(arr[0]))
print(solution(arr[1]))
print(solution(arr[2]))
print(solution(arr[3]))

print(row_solution(arr[0]))
print(row_solution(arr[1]))
print(row_solution(arr[2]))
print(row_solution(arr[3]))