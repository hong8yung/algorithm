vect = []
def solution(n, computers):
    network = []
    for i in range(n):
        network.append({i})

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                print(i, j, network)
                for idx, com in enumerate(network):
                    if i in com:
                        idx_1 = idx
                    if j in com:
                        idx_2 = idx
                if idx_1 != idx_2:
                    tmp = network[idx_1] | network[idx_2]
                    network.pop(max(idx_1, idx_2))
                    network.pop(min(idx_1, idx_2))
                    network.append(tmp)
    return len(network)

n = [3, 3]
computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]

print(solution(n[0], computers[0]))
print(solution(n[1], computers[1]))

#case0: 2
#case1: 1
