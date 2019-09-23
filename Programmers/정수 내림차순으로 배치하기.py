def solution(n):
    numbers = [str(x) for x in str(n)]
    numbers = sorted(numbers, reverse=True)

    tmp = ""
    for x in numbers:
        tmp += x

    return int(tmp)

def idle_solution(n):
    numbers = list(str(n))
    numbers.sort(reverse = True)
    return int("".join(numbers))

n = [118372]

print(solution(n[0]))

#case0: 873211
