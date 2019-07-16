from itertools import permutations

def chk_fnc(item, in_num, in_s, in_b):
    cnt_s = 0
    for i in range(3):
        if item[i]==in_num[i]:
            cnt_s += 1
    
    if not in_s == cnt_s:
        return False

    cnt_b = len(set(item) & set(in_num)) - cnt_s
    if not in_b == cnt_b:
        return False

    return True

def solution(baseball):
    answer = 0
    ans_arr = list(permutations([str(x) for x in range(1, 10)], 3))
    no_arr = set()
    for input_item in baseball:
        no_arr.clear()
        for item in ans_arr:
            if not chk_fnc("".join(item), str(input_item[0]), input_item[1], input_item[2]):
                no_arr.add(item)
            
        ans_arr = list(set(ans_arr) - no_arr)
    answer = len(ans_arr)
    return answer

tet_arr = [[123,1,1],  [356,1,0], [327,2,0], [489,0,1]]
print(solution(tet_arr))