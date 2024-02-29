import random

Rock_Paper_Scissors = ['가위', '바위', '보']
user_RPS = input('가위, 바위, 보를 고르세요: ')
com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
win_loss_record = [0, 0, 0]


def com_win():
    print('컴퓨터 승리!')
    win_loss_record[2] += 1


def user_win():
    print('사용자 승리!')
    win_loss_record[0] += 1


def end_game():
    print('게임을 끝냅니다')
    print(
        f'승:{win_loss_record[0]} 무:{win_loss_record[1]} 패:{win_loss_record[2]}')


while True:
    if user_RPS == com_RPS:
        print('무승부')
        win_loss_record[1] += 1
        yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
        if yes_or_no == 'y':
            user_RPS = input('가위, 바위, 보를 고르세요: ')
            com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
            continue
        else:
            end_game()
            break
    elif user_RPS == '가위':
        if com_RPS == '바위':
            com_win()
            yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
            if yes_or_no == 'y':
                user_RPS = input('가위, 바위, 보를 고르세요: ')
                com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
                continue
            else:
                end_game()
                break
        elif com_RPS == '보':
            user_win()
            yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
            if yes_or_no == 'y':
                user_RPS = input('가위, 바위, 보를 고르세요: ')
                com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
                continue
            else:
                end_game()
                break
    elif user_RPS == '바위':
        if com_RPS == '가위':
            user_win()
            yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
            if yes_or_no == 'y':
                user_RPS = input('가위, 바위, 보를 고르세요: ')
                com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
                continue
            else:
                end_game()
                break
        elif com_RPS == '보':
            com_win()
            yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
            if yes_or_no == 'y':
                user_RPS = input('가위, 바위, 보를 고르세요: ')
                com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
                continue
            else:
                end_game()
                break
    elif user_RPS == '보':
        if com_RPS == '가위':
            com_win()
            yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
            if yes_or_no == 'y':
                user_RPS = input('가위, 바위, 보를 고르세요: ')
                com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
                continue
            else:
                end_game()
                break
        elif com_RPS == '바위':
            user_win()
            yes_or_no = input("다시 플레이하시겠습니까?(Y/N): ").lower()
            if yes_or_no == 'y':
                user_RPS = input('가위, 바위, 보를 고르세요: ')
                com_RPS = Rock_Paper_Scissors[random.randint(0, 2)]
                continue
            else:
                end_game()
                break
    else:
        print('유효하지 않은 입력입니다')
        user_RPS = input('가위, 바위, 보를 고르세요: ')
        continue
