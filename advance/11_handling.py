num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]

idx = 0

try:
    while True:
        idx = num_list.index(3,idx) # ValueError: 3 is not in list
        print(f'3 은 {idx} 인덱스에 있습니다.')
        idx += 1
except ValueError:
    print('더이상 3을 찾을 수 없습니다.')
finally:
    print('====끝====')