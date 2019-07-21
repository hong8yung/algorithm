def solution(n):
    answer = ''
    tmp = []
    while n>0:
        tmp.insert(0, n%3)
        n = n//3
    
    #print(tmp)
    while 0 in tmp:
        for i in range(1, len(tmp)):
            if tmp[i] is 0:
                tmp[i] = 3
                tmp[i-1] -= 1
        if tmp[0] is 0:
            del tmp[0]

    tmp = [str(x) for x in tmp]
    answer = ''.join(tmp)
    answer = answer.replace('3', '4')
    return answer


n_1 = 1
n_2 = 2
n_3 = 3
n_4 = 4
n_5 = 10

print("{}의 결과값: {}".format(n_1, solution(n_1)))
print("{}의 결과값: {}".format(n_2, solution(n_2)))
print("{}의 결과값: {}".format(n_3, solution(n_3)))
print("{}의 결과값: {}".format(n_4, solution(n_4)))
print("{}의 결과값: {}".format(n_5, solution(n_5)))

for i in range(1, 30):
    print("{}의 결과값: {}".format(i, solution(i)))
