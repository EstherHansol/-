student=[]
score=[]
total = 0

inwon= int(input("학생 수 입력 :"))

for i in range(inwon) :
    name =input("학생이름: ")
    student.append(name)

print("우리반 학생 이름:", student)

for i in range (inwon):
    jumsu = int(input("%s성적 입력:"%(student[i])))
    score.append(jumsu)
    total=total + jumsu
    
print("우리반 학생 점수:", score)

print("총점: " , total, "평균:%2f"%(total /inwon))

