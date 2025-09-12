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


