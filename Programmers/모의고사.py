def solution(answers):
    answer = []
    ans_a = [1, 2, 3, 4, 5]
    ans_b = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    tmp = [0, 0, 0]
    for i in range(len(answers)):
        if ans_a[i%len(ans_a)] == answers[i]:
            tmp[0] += 1
        if ans_b[i%len(ans_b)] == answers[i]:
            tmp[1] += 1
        if ans_c[i%len(ans_c)] == answers[i]:
            tmp[2] += 1
            
    for i in range(len(tmp)):
        if tmp[i] == max(tmp):
            answer.append(i+1)
    return answer