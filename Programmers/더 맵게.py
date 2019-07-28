import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            break
        heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
        answer += 1

    if scoville[0] < K:
        answer = -1
    return answer

sc_1 = [1,2,3,9,10,12]

print(solution(sc_1, 7))