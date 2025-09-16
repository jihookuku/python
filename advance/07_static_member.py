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

# 원본의 내용을 고치고 싶다면? 원본으로 직접 가서 고쳐야 한다.
Robot.count = 1000
# 원본(static)영역에서 고쳤을때 당연히 복사본(heap)영역에는 영향이 없다.

print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r1.how_count()
r2.how_count()



