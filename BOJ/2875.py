import sys
inp = sys.stdin.readline

def greedy():
    girl, boy, internship = map(int, inp().split())

    return min(boy, int(girl/2), int((boy+girl-internship)/3))
if __name__ == "__main__":
    print(greedy())