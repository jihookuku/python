# 주석 = 컴퓨터는 알수 없고, 사람만 알수 있는 언어
# 이름 = 값
int = 123 # 정수
float = 3.14 #실수
octal = 0o117 # 8진수(숫자 0과 알파벳 o를 추가)
hex = 0x8ff # 16진수(숫자 0과 알파벳 x를 추가)

# print('int : '+int) # 문자+숫자 형태로는 출력해주지 않는다.
#f-string 을 사용하면 문자열과 다른 타입의 데이터를 함께 출력할 수 있다.
print(f'int: {int}')
print(f'float:{float}')
print(f'octal:{octal}')
print(f'hex:{hex}')
