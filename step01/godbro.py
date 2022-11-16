print("----------▶구구단 시작◀----------- \n")

for a in range(1, 10):
    print("------- [" + str(a) + "단] -------")
    for b in range(1, 10):
        print("{}*{}={}".format(a, b, a*b))

print("----------▶구구단 끝◀-----------")