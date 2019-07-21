import math
#fail
def solution(progresses, speeds):
    answer = []
    idx = 0
    tmp = 0
    while idx < len(progresses):
        while progresses[idx] < 100:
            for i in range(idx, len(progresses)):
                progresses[i] += speeds[i]
        tmp = 0
        for i in range(idx, len(progresses)):
            if progresses[i] >= 100:
                tmp += 1
                idx = i+1
        if tmp != 0:
            answer.append(tmp)
    return answer

def solution2(progresses, speeds):
    answer = []
    idx = 0

    while sum(answer) < len(progresses):
        day = math.ceil((100 - progresses[idx])/speeds[idx])
        tmp = 0
        for i in range(idx, len(progresses)):
            if (progresses[i] + (day*speeds[i])) >= 100:
                tmp += 1
                idx = i+1
            else:
                break
            
        if tmp != 0:
            answer.append(tmp)

    return answer   

progresses_1 = [93, 30, 55]
speeds_1 = [1, 30, 5]

print("결과값: {}".format(solution2(progresses_1, speeds_1)))