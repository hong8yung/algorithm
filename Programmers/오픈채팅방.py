def solution(record):
    log = {}
    answer = []
    record = [x.split() for x in record]
    for stat in record:
        if(stat[0]=="Enter") or (stat[0]=="Change"):
            log[stat[1]] = stat[2]

    for stat in record:
        if(stat[0]=="Enter"):
            answer.append("{}님이 들어왔습니다.".format(log[stat[1]]))
        elif(stat[0]=="Leave"):
            answer.append("{}님이 나갔습니다.".format(log[stat[1]]))

    return answer

record = [['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan']]

print(solution(record[0]))

#["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]