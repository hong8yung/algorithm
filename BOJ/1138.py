import sys
inp = sys.stdin.readline

class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next)
        self.size += 1

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, end=' ')
            else:
                print(p.item)
            p = p.next
    
    def inputCountNum(self, item, count):
        if self.is_empty():
            self.head = self.Node(item, None)
            self.size += 1
            return

        current_count = 0
        p = self.head
        # 해당 부분에서 리스트 순회하며 current_count 체크
        while p:
            if p.item > item:
                current_count += 1
            
            if count == current_count:
                self.insert_after(item, p)
                return
            else: 
                p = p.next

def greedy():
    numList = []
    res = []
    num = int(inp())
    numList = list(inp().split())

    for i, e in enumerate(numList):
        res.append((i+1, int(e))) 

    res = reversed(res)
    res = sorted(res, key=lambda number: number[1])

    resultList = SList()
    resultList.insert_after

    for i in res:
        number = i[0]
        count = i[1]

        resultList.inputCountNum(number, count)

    resultList.print_list()

if __name__ == "__main__":
    greedy()