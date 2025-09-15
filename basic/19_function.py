# 함수선언(define)
def toaster(bread):
    print(f'{bread} 이 구워지고 있다.')
    return f'구워진 {bread}'

# 함수 사용
dish = toaster('식빵')
print(dish)