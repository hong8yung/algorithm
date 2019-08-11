def solution(s):
    tmp = [int(i) for i in s.split()]
    return str(min(tmp))+" "+str(max(tmp))

s = ["1 2 3 4", "-1 -2 -3 -4", "-1 -1"]
print(solution(s[0]))
print(solution(s[1]))
print(solution(s[2]))
