answer = 0
def solution(numbers, target):
    tarNum(numbers, target, 0, 0)
    return answer

def tarNum(numbers, target, sum, idx):
    global answer
    if idx == len(numbers):
        if(sum == target):
            answer += 1
    else:
        tarNum(numbers, target, sum+numbers[idx], idx+1)
        tarNum(numbers, target, sum-numbers[idx], idx+1)

def idle_solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return idle_solution(numbers[1:], target-numbers[0]) + idle_solution(numbers[1:], target+numbers[0])

numbers = [[1, 1, 1, 1, 1]]
target = [3]

print(idle_solution(numbers[0], target[0]))
print(solution(numbers[0], target[0]))

#case0: 5
