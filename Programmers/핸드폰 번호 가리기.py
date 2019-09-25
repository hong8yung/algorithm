def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

phone_number = ["01033334444", "027778888"]

print(solution(phone_number[0]))
print(solution(phone_number[1]))