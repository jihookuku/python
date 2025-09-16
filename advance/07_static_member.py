class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드 : {self.count}')

    def std_count(self):
        print(f'클래스 메서드 : {self.count}')