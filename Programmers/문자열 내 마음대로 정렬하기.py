def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer

strings = [['sun', 'bed', 'car'], ['abce', 'abcd', 'cdx']]
n = [1, 2]

print(solution(strings[0], n[0]))
print(solution(strings[1], n[1]))

#case0: ['car', 'bed', 'sun']
#case1: ['abcd', 'abce', 'cdx']
