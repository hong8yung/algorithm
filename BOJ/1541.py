str = input()
tmpNum = ""
preNum = 0
preArr = []

for i in str:
    if i.isdigit():
        tmpNum += i
    else:
        preNum = preNum + int(tmpNum)
        if i == '-':
            preArr.append(preNum)
            preNum = 0
        tmpNum = ""
    
preNum = preNum + int(tmpNum)
preArr.append(preNum)

preNum = preArr[0]
for i in range(1,len(preArr)):
    preNum -= preArr[i]

print(preNum)