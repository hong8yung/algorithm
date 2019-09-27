def solution(num):
    idx = 0
    while 1:
        if idx >= 500:
            return -1
        if num == 1:
            return idx

        if num%2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

        idx += 1

n = [6, 16, 626331]

print(solution(n[0]))
print(solution(n[1]))
print(solution(n[2]))

#case0: 8
#case1: 4
#case2: -1
