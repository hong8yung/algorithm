def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            tmp = 'Z'
        elif i.islower():
            tmp = 'z'
        else:
            answer += i
            continue
        
        if ord(i)+n > ord(tmp):
            n -= ord('z') - ord('a') + 1

        answer += chr(ord(i)+n)

    return answer

s = ['ABD', 'z', 'a B z']
n = [24, 1, 4]

print(solution(s[0], n[0]))
print(solution(s[1], n[1]))
print(solution(s[2], n[2]))

#case0: BC
#case1: a
#case2: e F d
