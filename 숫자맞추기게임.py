import random

num=random.randrange(1,21)
guess= 0
#마음대로 초기값 설정 guess값 가능
count = 0


while num != guess and count <5:
    guess = int(input("숫자 입력:"))

    if guess >num:
        print("입력한 숫자가 비밀의 숫자보다 큽니다.")

    if guess <num:
        print( "입력한 숫자가 비밀의 숫자보다 작습니다.")

    count = count+1

if num == guess :
    print("정답입니다.")
    
else:
    print("5번 기회 끝났습니다", "정답은", num,"입니다.")

