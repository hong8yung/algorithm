from sys import stdin
inp = stdin.readline

CMD = ["push", "pop", "size", "empty", "top"]

class m_Stack:
    def __init__(self):
        self.Stack_item = []
    
    def push(self, x):
        self.Stack_item.append(x)
        
    def pop(self):
        if self.empty():
            return -1
        else:
            tmp = self.Stack_item[-1]
            del self.Stack_item[-1]
            return tmp

    def size(self):
        return len(self.Stack_item)

    def empty(self):
        return not self.Stack_item
    def top(self):
        if self.empty():
            return -1
        else:
            return self.Stack_item[-1]


if __name__ == "__main__":
    N = int(inp())
    q = m_Stack()
    for i in range(N):
        inp_cmd = inp().split()
        if inp_cmd[0] == CMD[0]: # case <push num>
            q.push(inp_cmd[1])
        elif inp_cmd[0] == CMD[1]: # case <pop>
            print(q.pop())
        elif inp_cmd[0] == CMD[2]: # case <size>
            print(q.size())
        elif inp_cmd[0] == CMD[3]: # case <empty>
            print(1 if q.empty() else 0)
        elif inp_cmd[0] == CMD[4]: # case <top>
            print(q.top())