def solution(prices):
    answer = [0 for x in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                break
        answer[i] = j-i
    return answer

prices_1 = [1,2,3,2,3]

print("{}의 결과값: {}".format(prices_1, solution(prices_1)))