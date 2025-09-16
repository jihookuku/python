num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]

idx = 0
while True:
    idx = num_list.index(3,idx) # ValueError: 3 is not in list
    print(f'3 은 {idx} 인덱스에 있습니다.')
    idx += 1