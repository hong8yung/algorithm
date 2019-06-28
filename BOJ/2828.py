import sys
inp = sys.stdin.readline

def greedy():
    M, N = map(int, inp().split())
    num_apple = int(inp())
    start_bowl = 1
    result = 0
    for i in range(num_apple):
        drop_apple = int(inp())
        if start_bowl<=drop_apple and drop_apple<start_bowl+N:
            result += 0
        elif drop_apple<start_bowl:
            result += start_bowl - drop_apple
            start_bowl = drop_apple 
        elif start_bowl+N <=drop_apple:
            result += drop_apple - (start_bowl+N) + 1
            start_bowl = drop_apple - N +1

    return result
if __name__ == "__main__":
    print(greedy())