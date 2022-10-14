def fact(m):

    if m ==0:
        return 1
    return m*fact(m-1)


n= int (input("숫자 입력 :"))

sum=fact(n)

print("%d!의 값은 %d 입니다." %(n,sum))
