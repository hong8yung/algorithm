def solution(N, stages):
    num = len(stages)
    answer = [[x+1, 0] for x in range(N+1)]

    for stage in stages:
        answer[stage-1][1] += 1 

    for i in answer:
        try:
            i[1],num = i[1]/num, num-i[1]
        except ZeroDivisionError:
            i[1] = 0

    return [x[0] for x in sorted(answer[:-1], key=lambda a:a[1], reverse = True)]

N = [5, 4]
stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4, 4, 4, 4, 4]]

print(solution(N[0], stages[0]))
print(solution(N[1], stages[1]))

#case0: [3, 4, 2, 1, 5]
#case1: [4, 1, 2, 3]
