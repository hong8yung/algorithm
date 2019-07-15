import sys
inp = sys.stdin.readline

class Stack():
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return False
        else:
            self.items.pop()
            return True
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

if __name__=="__main__":
    N = int(inp())
    num_arr = []
    res = []

    for i in range(N):
        num_arr.append(int(inp()))

    stack = Stack()
    idx = 0
    for i in range(1, N+1):
        stack.push(i)
        res.append("+")

        while idx<N and stack.peek()==num_arr[idx]:
            stack.pop()
            res.append("-")
            idx += 1
    
    if not stack.is_empty():
        print("NO")
    else:
        for i in range(len(res)):
            print(res[i])

