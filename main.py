# 모듈에 함수까지 전부 불러와서 사용하는 방법
from com.py.oop.other_module import other_function
other_function()

#모듈을 불러와서 별칭을 주어서 사용하는 방법
from com.py.oop import other_module as mo
mo.other_function()