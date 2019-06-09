import sys
inp = sys.stdin.readline

def greedy():
    coinArr = []
    result = 0
    coinNum, price = map(int, inp().split())
    for i in range(coinNum):
        coinArr.append(int(inp()))

    for coin in reversed(coinArr):
        result += int(price/coin)
        price = price % coin

    return result

if __name__ == "__main__":
    print(greedy())