from sys import stdin
inp = stdin.readline

def cut_stick(x):
    return bin(x).count('1')
if __name__=="__main__":
    length = int(inp())
    print(cut_stick(length))