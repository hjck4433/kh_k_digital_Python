# 회원정보 입력
# 이름/ 나이/ 성별/ 직업 / 결과 출력
# name = input("이름 : ")
# while 1 :
#     age = int(input("나이 : "))
#     if 0 < age < 200 : break
#     print("나이를 잘 못 입력 하셨습니다.")
#
# while 1 :
#     gender = input("성별 : ")
#     if gender == "M" or gender == "m" :
#         gender ="남성"
#         break
#     elif gender == "F" or gender == "f":
#         gender = "여성"
#         break
#     else :
#         print("성별을 잘 못 입력 하셨습니다.")
#
# while True :
#     jobs = int(input("직업 1(학생), 2(회사원), 3(주부), 4(무직) : "))
#     if jobs == 1:
#         jobs_str = "학생"
#         break
#     elif jobs == 2:
#         jobs_str = "회사원"
#         break
#     elif jobs == 3:
#         jobs_str = "주부"
#         break
#     elif jobs == 4:
#         jobs_str = "무직"
#         break
#     else:
#         print("잘못 선택 하셨습니다.")
# print(f"{name}님의 나이는 {age}, 성별은 {gender}, 직업은 {jobs_str} 입니다.")


# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

a = int(input("정수 A : "))
b = int(input("정수 B : "))
c = int(input("정수 C : "))

d = a * b * c
str_d = str(d)

for i in range(0,10) :
    cnt = 0
    for j in str_d:
        if i == int(j) : cnt += 1
    print(cnt)

# Y요금제 30 / 10   M요금제 60 / 15 // 3 | 40 40 40 | M 45
# n = int(input("통화 횟수 : "))
# num_str = input().split()
# y_pay = 0
# m_pay = 0
# for i in num_str :
#     y_time = (int(i) // 30) + 1
#     y_pay += y_time * 10
#
#     m_time = (int(i) // 60) + 1
#     m_pay += m_time * 15
## 입력한 통화 횟수만큼만 돌리기
# for i in range (0,n) :
#     y_time = (int(num_str[i]) // 30) + 1
#     y_pay += y_time * 10
#
#     m_time = (int(num_str[i]) // 60) + 1
#     m_pay += m_time * 15
#
# if y_pay == m_pay : print(f"YM {y_pay}")
# elif y_pay > m_pay : print(f"M {m_pay}")
# else : print(f"Y {y_pay}")


#대소문자 바꾸기
# word = input("단어 입력 : ")
#
# for i in word :
#     if i.isupper() :
#         print(i.lower(), end="")
#     else : print(i.upper(), end="")
#
# for i in word :
#     if ord(i) < ord("a") : print(i.lower(), end="")
#     else : print(i.upper(), end="")
