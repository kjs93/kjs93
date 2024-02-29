# 추상화 : abstraction
# 불필요한 정보는 숨기고 중요한 정보만을 표현
# 공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것

class Robot:
    # 클래스 변수 : 인스턴스들이 공유하는 변수

    population = 0
    # 생성자 함수 셀프는 각각의 인자(인스턴스)
    def __init__(self, name, code):
        self.name=name # 인스턴스 변수
        self.code=code # 인스턴스 변수
        Robot.population+=1

    #인스턴스 메서드
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a+b
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population-=1
        if Robot.population==0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robot working")

    @classmethod
    def how_many(cls):
        print(f"We have Robot {cls.population} robots.")

print(Robot.population) # 0
siri=Robot("siri", 21039788127)
print(Robot.population) # 1
jarvis=Robot("jarvis", 2311213123)
bixby=Robot("bixby", 124312423)
Robot.die(siri)

print(jarvis.__dict__)

print(Robot.__doc__)