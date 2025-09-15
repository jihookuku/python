# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능
def plus(num=0):
    result = num + 5
    return result

print(plus(5)) #10
print(plus()) # plus() missing 1 required positional argument: 'num'

# 인자값의 종류를 튜플(수정이 불가능한 List 형태)로만 받겠다.
def tuple_args(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total

# 이 방식은 사용자가 인자값의 갯수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1,2,3,4,5))

# ** 는 매개변수를 사전형태로 받겠다.
def dic_args(**dic):
    # 1. dic 에서 값만 빼온다.
    values = dic.values()
    #print(values)
    # 2. 이 값들을 하나씩 더해 누적시킨다.
    total = 0
    for v in values:
        #print(v)
        total += v
    # 3. 누적시킨 값을 밖으로 return 한다.
    return total
# 위 함수를 실행하면 입력된 값들의 합산이 반환되도록 하세요
result = dic_args(kim=50, lee=100, park=70, na=90)
print(result)


















