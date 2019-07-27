def solution(a, b):
    day_arr = ['THU', 'FRI', 'SAT', 'SUN','MON', 'TUE', 'WED']
    mon_arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mon_sum = 0
    if a is not 1:
        mon_sum = sum(mon_arr[:a-1])
        
    return day_arr[(mon_sum+b)%len(day_arr)]

print(solution(5, 25))