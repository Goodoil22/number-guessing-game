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
            continue
        attempts += 1
        if guess < answer:
            print("더 큰 수!")
        elif guess > answer:
            print("더 작은 수!")
        else:
            print(f"🎉 정답! {attempts}번 만에 맞췄어요!")
            break
    except ValueError:
        print("숫자만 입력하세요!")
else:
    print(f"😢 실패! 정답은 {answer}였어요.")

# 최고 점수 기록
try:
    with open("scores.txt", "r") as f:
        best = int(f.read())
except:
    best = 999

if attempts < best:
    with open("scores.txt", "w") as f:
        f.write(str(attempts))
    print(f"🥇 새 기록! {attempts}번")
else:
    print(f"최고 기록: {best}번")