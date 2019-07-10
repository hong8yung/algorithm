import itertools
def chk(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    tmp_list = []
    for i in range(1, len(numbers)+1):
        for number in itertools.permutations(numbers, i):
            if chk(int("".join(number))):
                tmp_list.append(int("".join(number)))
                
    answer = len(set(tmp_list))
    return answer

ret1 = "17"
ret2 = "011"

print(solution(ret1))
print(solution(ret2))