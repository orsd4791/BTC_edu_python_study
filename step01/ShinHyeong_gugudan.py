print("----------▶구구단 시작◀-----------")

while True:
    a = int(input("▶ 단 수 : "))
    if a > 0 and a <= 9 :
        print("------- [" + str(a) + "단] -------")
        for b in range(1, 10):
            print("{}*{}={}".format(a, b, a*b))
    elif a >= 10 and a < 17:
        print("------- [" + str(a) + "단] -------")
        for c in range(1, a+1):
            print("{}*{}={}".format(a, c, a*c))
    else:
        print("----------▶구구단 끝◀-----------")
        break