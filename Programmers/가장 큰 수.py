def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=lambda x: len(str(x)))
    max_cnt = len(str(numbers[-1]))
    numbers = sorted(numbers, key=lambda x: x*10**(max_cnt-len(str(x))), reverse=True)

    for i in numbers:
        answer += str(i)
    answer = str(int(answer))
    return answer

num_1 = [6, 1000, 10, 0, 2]
num_2 = [30, 3, 34, 5 ,9]
num_3 = [0,0,0]
num_4 = [40, 403]

num_5 = [40, 405]
num_6 = [40, 404]
num_7 = [12, 121]
num_8 = [2, 22, 223]
num_9 = [21, 212]
num_10 = [41, 415]
num_11 = [2, 22]
num_12 = [70, 0, 0, 0]
num_13 = [0, 0, 0, 0]
num_14 = [12, 1213]

print(solution(num_4))
print(solution(num_5))
print(solution(num_6))
print(solution(num_7))
print(solution(num_8))
print(solution(num_9))
print(solution(num_10))
print(solution(num_11))
print(solution(num_12))
print(solution(num_13))
print(solution(num_14))