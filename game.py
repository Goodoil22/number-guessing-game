import random

print("🎯 숫자 맞추기 게임!")
print("1~100 사이 숫자를 맞춰보세요.")

answer = random.randint(1, 100)
attempts = 0  # ← 이 줄 추가!

while True:
    guess = int(input("숫자 입력: "))
    attempts += 1  # ← 시도 횟수 증가
    if guess < answer:
        print("더 큰 수!")
    elif guess > answer:
        print("더 작은 수!")
    else:
        print(f"🎉 정답! {attempts}번 만에 맞췄어요!")  # ← 결과 출력 변경
        break