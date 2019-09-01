def solution(s):
    answer = ''
    flag = False
    for i, x in enumerate(s):
        if x == ' ':
            flag = True
        elif i is 0 or flag:
            flag = False
            if x.isalpha:
                x = x.upper()
        else:
            if x.isalpha:
                x = x.lower()
        answer += x

    return answer

s = ['3people unFollowed me', 'for the last week']

print(solution(s[0]))
print(solution(s[1]))

#case0: 3people Unfollowed Me
#case1: For The Last Week
