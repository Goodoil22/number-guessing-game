import random

print("🎯 숫자 맞추기 게임!")
print("1~100 사이 숫자를 맞춰보세요.")

answer = random.randint(1, 100)
while True:
    guess = int(input("숫자 입력: "))
    if guess < answer:
        print("더 큰 수!")
    elif guess > answer:
        print("더 작은 수!")
    else:
        print("🎉 정답!")
        break