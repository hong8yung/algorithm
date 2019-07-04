from sys import stdin
inp = stdin.readline

def chkprnt(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False

            stack.pop()
        
    return True if len(stack)==0 else False

if __name__ == "__main__":
    N = int(inp())
    for i in range(N):
        tmp = (inp().split())[0]
        if chkprnt(tmp):
            print("YES")
        else:
            print("NO")