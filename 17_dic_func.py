dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends':['Alice','Smith','Jhone']
}

# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys 라는 객체를 반환한다.
print(dic.keys())

for item in dic.keys():
    print(item)

# dict_keys -> list 로 변환
keys = list(dic.keys());
print(keys)

# dic.values() : 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())
# list 로 변경해서 values 라는 변수에 담아보자
values = list(dic.values())
print(values)

# dic.items() : 사전의 키:값 을 한 쌍으로가져와 dict_items 로 반환한다.
# 각 키와 값은 () 모양으로 보아 tuple 이다.
print(dic.items())
# list 로 변환해 보면 list 안에 각 키와 값이 튜플로 저장되어 있음을 알 수 있다.
li = list(dic.items())
print(li)

# 값을 가져오기(택1)
print(dic.get('name'))
print(dic['phone'])

# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해 보자
# 1. 키를 뽑아낸다음, 키를가지고 값을 뽑아내는 방법
for key in dic.keys():
    print(f'{key}:{dic[key]}')

# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for item in dic.items():
    print(f'{item[0]}={item[1]}')

members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

# 90이상인 사람의 이름만 출력
for item in members.items():
    if item[1] >=90:
        print(f'이름 : {item[0]}')










