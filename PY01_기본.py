print("Hello, world")
print('Hello, world')
print(100)
print(33.33)
print(100+23)

# 변수를 선언하고 값을 대입
num = 100   # 데이터형은 값이 대입되는 순간에 결정 남
print(num)
num = "100"
# 여기는 주석 입니다.
'''
여기는 범위 주석 구간 입니다.
'''

# 변수 활용
name = "레몬레몬"
email = "hjck4433@gmail.com"
age = 32
addr = '서울시 강남구 역삼동 KH정보교육원'

print(f"""
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
""")

# 파이썬은 불리언 값이 대문자로 시작
isAdult = True

# 들여쓰기를 지켜줘야 함 (빈칸 수 일정하게)
if isAdult :
    print("나는 성인 입니다.")
else :
    print("나는 성인이 아닙니다.")
