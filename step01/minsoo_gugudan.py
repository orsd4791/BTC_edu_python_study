while True:
    dan = int(input("1-16 사이의 단을 입력하세요 : "))

    if 1 <= dan and dan < 10:
        print(f':: {dan}단 ::')
        for i in range(1, 10):  # 1 ~ 9
            print(f'{dan} x {i} = {dan * i}')
        print('-'*10)
        continue
    elif 10 <= dan and dan <= 16:
        print(f':: {dan}단 ::')
        for i in range(1, dan+1):  # 1 ~ 9
            print(f'{dan} x {i} = {dan * i}')
        print('-' * 10)
        continue
    else:
        print("1-16 사이의 단을 입력하세요 !!!")
        continue