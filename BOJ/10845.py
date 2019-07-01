from sys import stdin
inp = stdin.readline

CMD = ["push", "pop", "size", "empty", "front", "back"]

class m_Queue:
    def __init__(self):
        self.Queue_item = []
    
    def push(self, x):
        self.Queue_item.append(x)
        
    def pop(self):
        if self.empty():
            return -1
        else:
            tmp = self.Queue_item[0]
            del self.Queue_item[0]
            return tmp

    def size(self):
        return len(self.Queue_item)

    def empty(self):
        return not self.Queue_item

    def front(self):
        if self.empty():
            return -1
        else:
            return self.Queue_item[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.Queue_item[-1]


if __name__ == "__main__":
    N = int(inp())
    q = m_Queue()
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
        elif inp_cmd[0] == CMD[4]: # case <front>
            print(q.front())
        elif inp_cmd[0] == CMD[5]: # case <back>
            print(q.back())
