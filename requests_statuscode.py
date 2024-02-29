# 사각형 만들기

# 클래스 선언
class Qurd():
    height = 0
    width = 0
    color = ''
    name='Qurd'

    def qurd_name(self):
        return self.name

# 객체 생성
qurd1=Qurd()
qurd2=Qurd()

# 객체 기능 호출
qurd1.width=10
qurd1.height=10
qurd1.color='blue'
qurd1.name='blue 사각형'

qurd2.width=5
qurd2.width=5
qurd2.color='yellow'
qurd2.name='yellow 사각형'

print(qurd1.name,qurd2.name)