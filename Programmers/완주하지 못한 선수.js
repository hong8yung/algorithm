function solution(participant, completion){
    var answer = '';
    participant.sort();
    completion.sort();
    for(var i in completion){
        if(participant[i] != completion[i]){
            answer = participant[i];
            break;
        }
    }
    return answer;
}

par =[["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]]
compl = [["eden", "kiki"],["josipa","filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]]

console.log(solution(par[0], compl[0]))