# set 은 순서가 없고, 중복을 허용하지 않는다.
number_set = set([1,2,3])
print(number_set)

# 중복을 제외하고 담는다.
# 그래서 중복 제거용도로 사용된다.
str_set = set("HelloWorld")
print(str_set)

# set 들을 이용해서 집합을 구현할 수 있다.
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합(intersection)
print(f'교집합1 : {s1 & s2}')
print(f'교집합2 : {s1.intersection(s2)}')

#합집합(union)
print(f'합집합1:{s1|s2}')
print(f'합집합2:{s1.union(s2)}')

#차집합(minus|difference)
print(f'차집합:{s1-s2}')
print(f'차집합:{s2-s1}')

# 값 1개 추가하기
s1.add(10)
print(s1)

# 여러개 추가하기
s1.update([10,20,30])
print(s1)

# 특정값 제거
s1.remove(10)
print(s1)
# s1.remove(10) <- 없는 값을 지우려고 하면 KeyError 발생
s1.discard(10) # remove 와 같으나 없는 값을 지우려고 해도 에러가 나지 않는다.








