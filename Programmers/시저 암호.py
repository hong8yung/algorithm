def idel_solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))

        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

def solution(s, n):
    answer = ''
    k = ord('z') - ord('a') + 1
    for i in s:
        if i.isupper():
            if (ord(i)+n) > ord('Z'):
                answer+=chr(ord(i)+n-k)
            else:
                answer += chr(ord(i)+n)
        elif i.islower():
            if (ord(i)+n) > ord('z'):
                answer+=chr(ord(i)+n-k)
            else:
                answer += chr(ord(i)+n)
        else:
            answer += i
            continue

    return answer

s = ['ABD', 'z', 'a B z']
n = [24, 1, 4]

print(solution(s[0], n[0]))
print(solution(s[1], n[1]))
print(solution(s[2], n[2]))

#case0: BC
#case1: a
#case2: e F d
