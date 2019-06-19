import sys
inp = sys.stdin.readline

orgnPay = 1000

def greedy():
    res = 0
    coinArr = [500, 100, 50, 10, 5, 1]
    amntPay = int(inp())
    chng = orgnPay - amntPay

    for i in coinArr:
        if(chng == 0):
            break
        res += int(chng/i)
        chng -= int(chng/i) * i

    return res

if __name__ == "__main__":
    print(greedy())
