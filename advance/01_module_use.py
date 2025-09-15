# from 모듈 import 함수
# 사용할 함수를 미리 불러놓고 사용하는 방법
from oper import sum
print(f'sum() 함수 실행 : {sum(5,10)}')

# import 모듈
# 일단 모듈을 불러놓고 모듈로부터 원하는 함수를 사용하는 방법
import oper as op
print(f'minus() 함수실행 : {op.minus(10,5)}')

# 변수도 불러다 사용 할 수 있다.
print(f'filed1 : {op.field1} / filed2 : {op.field2}')