class Car:
    def start(self):
        print('시동이 걸린다.')

    def run(self):
        print('차가 시속 50km 로 달린다.')

    def stop(self):
        print('차가 멈춘다.')

class MyCar(Car):

    def run(self): # 부모와 같은 메서드를 사용하면 override 로 인식된다.
        print('차가 시속 200km 로 달린다.')


mc = MyCar()
mc.start()
mc.run()
mc.stop()