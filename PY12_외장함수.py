# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함.
import random

# randint(0, 4) : 0 ~ 4 까지의 임의의 정수값이 반환 (0~4)
# randrange(0, 4) : 0 ~ 4 미만의 임의의 정수값이 반환 (0~3)

# for i in range(100) :
#     rand = random.randint(0, 4)
#     print(rand)
# 
# for i in range(100) :
#     rand = random.randrange(0, 4)
#     print(rand)
    
# 현재 시간 가져오기
# from datetime import datetime # datetime 모듈에서 datetime 함수만 import 함
# print(datetime.today()) # 현재 날짜 가져오기
# print(datetime.today().year) # 현재 연도 가져 오기
# print(datetime.today().month)
# print(datetime.today().day)
# print(datetime.today().hour)
# print(datetime.today().minute)
# print(datetime.today().second)
# 
# # 수학 계산을 위한 math
# import math
# print(math.sin(100)) # 사인값
# print(math.cos(100)) # 코사인
# print(math.tan(100)) # 탄젠트
# print(math.log(100)) # 로그
# print(math.ceil(100.1)) # 무조건 올림
# print(math.floor(100.99999)) # 무조건 내림

# 중복 값이 없는 로또 번호 생성하기
import random
print("로또 번호 자동 생성기")
ls = [] # 빈 리스트 만들기
while True :
    rand = random.randrange(1,46)
    if rand not in ls: # list에 생성된 rand값이 포함되어 있지 않으면
        ls.append(rand)
    if len(ls) == 6: break
print(ls)