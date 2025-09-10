import random

number = random.randint(1,31)
print(f' 내 마음속 숫자: {number}')
running = True


while running:
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
    print(f'입력받은 숫자 : {guess}')
    if number > guess:
        print('내가 생각한 숫자보다 작습니다.')
    elif number < guess:
        print('내가 생각한 숫자보다 큽니다.')
    else:
        print('정답입니다.')
        running = False