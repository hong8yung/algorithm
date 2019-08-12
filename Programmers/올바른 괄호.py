def solution(s):
    answer = True
    tmp = []

    for i in s:
        if i is "(":
            tmp.append(i)
        elif len(tmp) is not 0:
            tmp.pop()
        else:
            answer = False
    
    if len(tmp) is not 0:
        answer = False
    
    return answer

s=["()()","(())()",")()(","(()("]
for i in s:
    print(solution(i))