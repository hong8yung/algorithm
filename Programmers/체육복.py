def solution(n, lost, reserve):
    answer = 0

    and_set = set(lost) & set(reserve)
    lost = list(set(lost) - and_set)
    reserve = list(set(reserve) - and_set)

    lost.sort()
    reserve.sort()

    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            continue
        n -= 1

    answer = n
    return answer

ret1 = solution(5, [2,4], [1,3,5])
ret2 = solution(5, [2,4], [3])
ret3 = solution(3, [3], [1])

print(ret1, ret2, ret3)
