def solution(citations):
    answer = 0
    for i in range(max(citations), 0, -1):
        tmp = 0
        for citation in citations:
            if citation >= i:
                tmp += 1
            if tmp == i:
                return tmp

    return answer

cit = [3, 0, 6, 1, 5]

print(solution(cit))