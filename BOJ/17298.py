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
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

if __name__ == "__main__":
    numbers = []
    stack = Stack()
    
    N = int(inp())
    numbers = list(map(int, inp().split()))
    result = [0 for x in range(N)]

    for idx in range(N-1, -1, -1):
        if not stack.is_empty():
            while stack.top() <= numbers[idx]:
                stack.pop()
                if stack.is_empty():
                    break

        if stack.is_empty():
            result[idx] = -1
        else:
            result[idx] = stack.top()
        
        stack.push(numbers[idx])

    for i in result:
        print(i, end=' ')