import random

print("🎯 숫자 맞추기 게임!")
difficulty = input("난이도 선택 (e:쉬움/10회, m:보통/7회, h:어려움/5회): ").lower()

if difficulty == "e":
    max_attempts = 10
    range_max = 100
elif difficulty == "m":
    max_attempts = 7
    range_max = 75
elif difficulty == "h":
    max_attempts = 5
    range_max = 50
else:
    print("기본(보통)으로 시작!")
    max_attempts = 7
    range_max = 75

print(f"1~{range_max} 숫자, 최대 {max_attempts}회 도전!")

answer = random.randint(1, range_max)
attempts = 0

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