### 11.16 과제 ####
## 구구단 ##

while True :
    print("16단 구구단 프로그램입니다.")
    num = int(input("단 수를 입력하시오. 종료하려면 0을 누르세요.\n 단 수: "))
    if num <= 0 | num >= 17 :
        if num == 0 :
            print("프로그램을 종료합니다.")
        print("수를 잘못 입력 하였습니다. 1~16으로 입력하시오")
    if num <= 9:
        for set in range(1,10):
            print("{0}*{1}={2}".format(num,set,num*set))
    if num >= 10:
        for set in range(1,num+1) :
            print("{0}*{1}={2}".format(num,set,num*set))
