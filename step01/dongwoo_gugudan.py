print("1 ~ 16까지 수를 입력 하세요~")
i = int(input())
j = 1
if i < 10 :
  while(j<10):
      k = i * j
      print(i," * ", j, " = ", k)
      j+=1
elif 9 < i < 17 :
  while(j<=i):
     k = i * j
     print(i," * ", j, " = ", k)
     j+=1
else :
  print(" 숫자 범위를 벗어남")
