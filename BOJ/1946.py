import sys
inp = sys.stdin.readline

def gen(num):
    for i in range(num):
        S = int(inp())
        records = []
        for j in range(S):
            a, b = map(int, inp().split())
            records.append((a,b))
        
        yield sorted(records)
    

def greedy(records):
    count = 0
    min = 100001
    for i, record in enumerate(records):
        if record[1] < min:
            min = record[1]
            count += 1
    
    return count

if __name__ == "__main__":
    T = int(inp())
    for records in gen(T):
        print(greedy(records))