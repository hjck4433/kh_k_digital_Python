# 제어문이란 ? 조건문과 반복문을 의미하며 순차적인 흐름을 제어하는 목적으로 사용 된다.
# n = int(input("정수를 입력 하세요 : "))
# if n > 100:
#     print(f"{n}은 100보다 커요")
# elif n < 100:
#     print(f"{n}은 100보다 작아요")
# else:
#     print(f"{n}은 100과 같아요")

# 조건문에서 문자열 비교
while 1:
    season = input("현재 계절을 입력 하세요 : ")
    if season == "spring" :
        print("봄이 왔어요")
        break
    elif season == "summer" :
        print("무더운 여름 입니다.")
        break
    elif season == "autumn" or season == "fall" :
        print("가을이 왔어요")
        break
    elif season == "winter" :
        print("추운 겨울 입니다")
        break
    else :
        print("계절을 잘못 입력 하셨습니다.") # 파이썬은 무조건 else로 끝나야 하고 내용이 있거나 pass
