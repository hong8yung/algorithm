def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack  = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1

            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer

def old_solution(n, computers):
    network = []
    for i in range(n):
        network.append({i})

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
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
