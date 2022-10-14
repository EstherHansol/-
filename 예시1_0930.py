rnum = input("강의실 번호: ")

if 'A' in rnum or 'a' in rnum:
    print("사범관")

elif 'B' in rnum or 'b' in rnum:
    print("미술관")

elif 'C' in rnum or 'c' in rnum:
    print("가정관")

else:
    print("우리학교 건물이 아닙니다.")
    
