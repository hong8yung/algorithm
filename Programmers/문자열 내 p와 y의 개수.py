def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')

s = ["pPoooyY", "Pyy"]

print(solution(s[0]))
print(solution(s[1]))

#case 1 : true
#case 2 : false