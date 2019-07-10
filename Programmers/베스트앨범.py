def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [0,[]]
        dic[genres[i]][0] += plays[i]
        dic[genres[i]][1].append((i, plays[i]))
    
    for i in sorted(dic, key=lambda x: dic[x][0], reverse=True):
        dic[i][1].sort(key=lambda x: x[1], reverse=True)
        for j in range(0, len(dic[i][1])):
            answer.append(dic[i][1][j][0])
            if j == 1:
                break
        
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500,600,150,800,2500]

res = solution(genres, plays)
print(res)