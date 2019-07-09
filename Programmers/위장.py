def solution(clothes):
    answer = 1
    tag = {}
    for i in clothes:
        if i[1] in tag:
            tag[i[1]] += 1
        else:
            tag[i[1]] = 1
    
    for i in tag:
        answer *= tag[i] + 1
            
    return answer - 1