def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, -1, -1):
        for j in range(i, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break

    return answer

hei_1 = [6,9,5,7,4]
hei_2 = [3,9,9,3,5,7,2]
hei_3 = [1,5,3,6,7,6,5]

print("{}의 결과값: {}".format(hei_1, solution(hei_1)))
print("{}의 결과값: {}".format(hei_2, solution(hei_2)))
print("{}의 결과값: {}".format(hei_3, solution(hei_3)))