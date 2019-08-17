def solution(arr):
    answer = []
    tmp = -1
    for i in arr:
        if tmp is not i:
            tmp = i
            answer.append(i)
        else:
            continue

    return answer

def idle_solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer

arr = [[1,1,3,3,0,1,1], [4,4,4,3,3]]
print(solution(arr[0]))
print(solution(arr[1]))