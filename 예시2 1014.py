def fact(m):

    if m ==1:
        return 1
    return m*fact(m-1)


n= int (input("숫자 입력 :"))

sum=fact(n)

print(sum)
