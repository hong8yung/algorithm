function solution(participant, completion){
    var answer = '';
    for(var i in completion){
        participant.splice(participant.indexOf(completion[i]), 1)
    }
    answer = participant[0]
    return answer;
}

par =[["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]]
compl = [["eden", "kiki"],["josipa","filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]]

console.log(solution(par[0], compl[0]))