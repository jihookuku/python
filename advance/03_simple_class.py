# java 에서는 파일명 == 클래스명
# 파이썬에서는 꼭 그렇진 않다.
class Student: # Student 라는 클래스(학생과 관련된 함수 및 면수가 들어오겠구나 라고 예측 가능)
    pass # pass 는 함수나 클래스에 아무것도 없을때 오류방지를 위해 넣는 키워드

std1 = Student()
std2 = Student()
std3 = Student()
# 일련번호가 서로 다르다.
# 파이썬 에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.
print(std1)
print(std2)
print(std3)