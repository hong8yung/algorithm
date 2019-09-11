def solution(s):
    result = 0
    for idx, i in enumerate(s[::-1]):
        if i == '-':
            result *= -1
        elif i == '+':
            pass
        else:
            result += (ord(i) - ord('0'))*(10**idx)

    return result

def old_solution(s):
    return int(s)

strTmp = ["1234", "-1234", "+1234"]

print(solution(strTmp[0]))
print(solution(strTmp[1]))
print(solution(strTmp[2]))