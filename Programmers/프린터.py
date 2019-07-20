def solution(priorities, location):
    answer = 0
    tmp_arr = [(idx,priorities[idx]) for idx in range(len(priorities))]

    while len(tmp_arr) > 0:
        if not tmp_arr[0][1] is max(priorities):
            tmp_arr.append(tmp_arr[0])
            del tmp_arr[0]
        else:
            #print this
            answer += 1

            if location is tmp_arr[0][0]:
                break

            del tmp_arr[0]
            priorities.remove(max(priorities))

    return answer

prio_1 = [2, 1, 3, 2]
location_1 = 2

prio_2 = [1, 1, 9, 1, 1, 1]
location_2 = 0

print("test case 1: {} -> {}".format((prio_1, location_1), solution(prio_1, location_1)))
print("test case 2: {} -> {}".format((prio_2, location_2), solution(prio_2, location_2)))

