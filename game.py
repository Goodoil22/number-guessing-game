import random

print("🎯 숫자 맞추기 게임!")
print("1~100 사이 숫자, 최대 10회 도전!")

answer = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input(f"({attempts+1}/{max_attempts}) 숫자 입력: "))
        if guess < 1 or guess > 100:
            print("1~100 사이로 입력하세요!")
            