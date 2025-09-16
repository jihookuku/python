class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드 : {self.count}')

    # 2. self 는 내가 소속된 객체를 의미하는데 원본에서 왔으므로 객체가 없다.
    # 3. @classmethod  어노테이션을 이용해 원본에서 직접 왔으므로 self 는 객체가 아닌 클래스라도 알려줌
    # 4. 그러니 self 라는 이름은 객체를 받는 인자값으로 오해할수 있으니 cls 로 바꾸라고 권고
    @classmethod 
    def std_count(cls):
        print(f'클래스 메서드 : {cls.count}')

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

#마찬가지로 원본의 내용을 확인하고 싶다면 원본영역으로 가서 확인해야 한다.
print(f'원본 count : {Robot.count}')

# 1. 원본영역에서 함수를 실행하니 self 가 없다고 에러가남
# TypeError: Robot.std_count() missing 1 required positional argument: 'self'
Robot.std_count()














