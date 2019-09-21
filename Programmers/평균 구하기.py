def solution(arr):
    if len(arr) == 0:
        return 0
    return sum(arr)/len(arr)

arr = [[1, 2, 3, 4], [5, 5]]

print(solution(arr[0]))
print(solution(arr[1]))

#case0: 2.5
#case1: 5
