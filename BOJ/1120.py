import sys
inp = sys.stdin.readline

def greedy():
    tmp = 0
    result = 50
    str_A, str_B = map(str, inp().split())
    minor = len(str_B) - len(str_A)
    for i in range(minor+1):
        tmp = 0
        for j in range(len(str_A)):
            if(str_A[j] != str_B[i+j]):
                tmp += 1
        result = min(tmp, result)
        print(i, minor, result)

    return result


if __name__ == "__main__":
    print(greedy())