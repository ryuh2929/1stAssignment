import random

number = int(input("1~100 사이의 숫자를 입력하세요: "))

rand_num = random.randint(1, 100)

print(rand_num)

repeat_count = 1

while repeat_count < 100:
    if number < 1 or number > 100:
        print('1에서 100사이의 숫자만 가능합니다')
        number = int(input("1~100 사이의 숫자를 입력하세요: "))
        continue
    elif number == rand_num:
        print('정답입니다')
        print(f'{repeat_count}번만에 맞추셨습니다')
        yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ")
        if yes_or_no == 'Y' or yes_or_no == 'y':
            number = int(input("1~100 사이의 숫자를 입력하세요: "))
            rand_num = random.randint(1, 100)
            print(rand_num)
            repeat_count = 1
            continue
        else:
            print('게임을 끝냅니다')
            break
    elif number > rand_num:
        print('DOWN')
    elif number < rand_num:
        print('UP')
    repeat_count += 1
    number = int(input("1~100 사이의 숫자를 입력하세요: "))
    continue
