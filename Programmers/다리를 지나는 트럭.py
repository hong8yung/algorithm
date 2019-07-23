def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = len(truck_weights)
    bridge_arr = [0] * bridge_length
    clear_arr = []
    while len(clear_arr) != cnt:
        if bridge_arr[0]!=0:
            clear_arr.append(bridge_arr.pop(0))
        else:
            bridge_arr.pop(0)

        if truck_weights:
            if sum(bridge_arr)+truck_weights[0] <= weight:
                bridge_arr.append(truck_weights.pop(0))
            else:
                bridge_arr.append(0)
        else:
            bridge_arr.append(0)

        answer += 1

    return answer

input_1 = [2, 10, [7,4,5,6]]
input_2 = [100, 100, [10]]
input_3 = [100, 100, [10,10,10,10,10,10,10,10,10,10]]

print(solution(input_1[0], input_1[1], input_1[2]))
print(solution(input_2[0], input_2[1], input_2[2]))
print(solution(input_3[0], input_3[1], input_3[2]))