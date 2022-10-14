print("영화관 입장료 계산하는 프로그램")

adult= int(input("성인 인원수를 입력해주세요:"))
youth= int(input("청소년 인원수를 입력해주세요:"))
kids= int(input("어린이 인원수를 입력해주세요:"))

if adult >0:
    sum= adult * 13000
    print("성인 :", adult, end=" , ")

if youth >0:
    sum= sum+(youth*11000)
    print("청소년:", youth,end=" , ")

if kids >0:
    print("어린이:", kids,end=" , ")

print(sum)
