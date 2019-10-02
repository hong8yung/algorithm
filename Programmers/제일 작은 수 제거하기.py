def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

arr = [[4, 3, 2, 1], [10]]

print(solution(arr[0]))
print(solution(arr[1]))

#case0: [4, 3, 2]
#case1: [-1]
