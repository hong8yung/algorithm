import sys
inp = sys.stdin.readline

if __name__ == "__main__":
    while True:
        result = True
        stack = []
        strline = inp().strip('\n')
        if strline == ".":
            break

        for i in strline:
            if i == '(' or i =='[':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    result = False
                    break
                else:
                    stack.pop()
            elif i == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    result = False
                    break
                else:
                    stack.pop()

        if result and len(stack) == 0:
            print("yes")
        else:
            print("no")

