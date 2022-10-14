dan= int(input("원하는 구구단: "))
updown=input("정렬 방식 A or D : ")
if 'A' in updown or 'a' in updown:
    i =1
    while i<10:
        print(dan, "*", i, "=", dan *i)
        i=i+1

elif 'D' in updown or 'd' in updown:
    i =9
    while i>0:
        print(dan, "*", i, "=", dan *i)
        i=i-1
    

else :
    print("정렬 다시 선택:")
