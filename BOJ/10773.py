from sys import stdin
inp = stdin.readline

if __name__ == "__main__":
    stack = []
    K = int(inp())

    for i in range(K):
        tmp = int(inp())
        if tmp == 0:
            stack.pop()
        else:
            stack.append(tmp)

    sum = 0
    for i in stack:
        sum += i
    
    print(sum)