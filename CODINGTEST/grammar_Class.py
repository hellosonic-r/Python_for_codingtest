###개념예시
class Singer: #가수를 정의하겠다.
    def sing(self): #노래하기 메서드
        return "Lalala~"
    
taeji = Singer() #태지 라는 객체를 만들어라 / 인스턴스명 = 클래스()
print(taeji.sing()) #함수결과 출력
                    #Singer 클래스에 sing 메서드를 정의했기 때문에 /
                    #Singer 클래스에 속한 태지 객체도 sing 메서드 사용 가능
                    #사용할때는 객체.메소드 로 사용

###예시
#Human 클래스 만들기
class Human:
    power = 5
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("나의 이름은",self.name,"이고, 나이는",self.age,"이고, 힘은",self.power,"입니다.")
human1 = Human("짱구", "10")
human2 = Human("철수", "12")
human1.power += 1

print(human1.info())
print(human2.info())
#왜 none이 출력되지?
#사칙연산 클래스 만들기
