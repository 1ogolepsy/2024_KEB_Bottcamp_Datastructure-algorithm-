import random

note = random.randint(1, 100)
count = 1
while True:
    n = int(input("숫자를 입력하세요."))
    if note < n:
        print("틀렸습니다! down")
    elif note > n:
        print("틀렸습니다! up")
    elif note == n:
        print(f"정답입니다. 총 {count}회 만에 맞추셨습니다.")
        break
    else:
        print("잘못된 값을 입력했습니다. 다시!!")

    count += 1