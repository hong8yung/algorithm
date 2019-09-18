def solution(s):
    if (len(s) != 4) and (len(s) != 6):
        return False
    else:
        for i in s:
            if not i.isnumeric():
                return False
        else:
            return True

s = ["a234", "1234"]
print(solution(s[0]))
print(solution(s[1]))