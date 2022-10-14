name = input("이름을 입력하세요:")
add=input("주소를 입력하세요:")
hobby=input("취미를 입력하세요:")

print("안녕",name,"님 반갑습니다.!")
print(name, "님은",add,"에 사시는군요")
print(name,"님은",hobby,"를 좋아하시는군요")

print("안녕 %s님 반갑습니다!" %(name))
print("%s님은 %s에 사시는군요 " %(name,add))
print("%s님은 %s를 좋아하시는군요" %(name, hobby))

radius=10
pi=3.141592

print("반지름 10일 :",radius*radius*pi)


radius=radius+10
print("반지름 20일 :",radius*radius*pi)

radius=radius+10
print("반지름 30일 :",radius*radius*pi)

radius=radius+10
print("반지름 40일 :",radius*radius*pi)

radius=radius+10
print("반지름 50일 :",radius*radius*pi)
