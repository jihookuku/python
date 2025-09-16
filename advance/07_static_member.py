class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드 : {self.count}')

    def std_count(self):
        print(f'클래스 메서드 : {self.count}')

r1 = Robot()
r2= Robot()
# r1 과 r2 는 서로 다른 객체이므로 count 를 건드렸을때 서로 영향받지 않는다.
r1.count += 1
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r2.count = 100
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')




