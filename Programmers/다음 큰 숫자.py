def solution(n):
    answer = 0
    num = str(bin(n)).count('1')
    for i in range(1, 1000001-n):
        if str(bin(i+n)).count('1') == num:
            answer = n+i
            break
    return answer

n = [78, 15]
print(solution(n[0]))
print(solution(n[1]))