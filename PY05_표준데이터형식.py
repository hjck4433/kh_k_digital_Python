# 값을 할당하는 방법
a = b = c = 1
print(a, b, c)

a, b, c = 1, False, "곰돌이사육사" # 여러개의 변수를 한번에 대입,
print(a, b, c)

# 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

value = 0o77 # 8진수
print(value) # 63

value2 = 0xFF # 16진수 => 컬러값이 16진수
print(value2) # 255

# 불리언 타입 : 참과 거짓의 값을 가짐
# True
print(bool(1))
print(bool(-100))
# False
print(bool(0))
print(bool(""))
print(bool(None))  # 값이 정해지지 않았음을 의미
print(bool())

# 문자열 타입 :
str1 = "Hello Python!!!!"
print(str1)
print(str1[0])  # 인덱싱
print(str1[2:5])  # 2번 인덱스에서 5번 인덱스 미만
print(str1[2:])  # 2번 인덱스부터 끝까지
print(str1 * 3)
print(str1 + "TEST")

# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨, 이후 데이터형을 변경하고자 할 때 형변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1 + 3.141592 + float("4.44"))
