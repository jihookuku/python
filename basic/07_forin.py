# for 문은 반복 횟수가 정해진 상태에 적합하다.

# 물 10잔 떠 오기
#for [하나씩가져올변수] in [범위]:
for cup in range(1, 11):
    print(f'물 {cup} 번째 잔 떠왔습니다.')

print()
# 만약 커피를 타는데 한잔의 물에 믹스 2개씩을 넣어야 한다면?
# 반복안에 반복이 발생된다.
for cup in range(1, 11):
    print(f'물 {cup} 번째 잔 떠왔습니다.')
    for mix in range(1,3):
        print(f'{mix} 개의 믹스를 넣는다.')
        for spoon in range(1,4):
            print(f'{spoon} 번 수픈으로 젖는다.')