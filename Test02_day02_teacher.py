# 1번 문제 : 세자리 정수를 입력 받은후 가장 큰 수 찾기 (123 => 3)
# n = int(input("정수 입력 : "))
# a = n // 100
# b = (n % 100) // 10
# c = n % 10
# if a > b:
#     if a > c : print(a)
#     else: print(c)
# else:
#     if b > c : print(b)
#     else: print(c)

# 2번 문제 : 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원
# 야간 근무 : 주간 시급 * 1.5
# 주간근무[1], 야간근무[2]를 입력 하세요 :
# 근무 시간을 입력해 주세요
# 입력한 시간 동안 근무한 주간 또는 야간 급여는 ____원 입니다.
# 근무타입 = int(input("주간근무[1], 야간근무[2]를 입력 하세요 : "))
# 근무시간 = int(input("근무 시간을 입력해 주세요 : "))
# if 근무타입 == 1 :
#     급여 = 근무시간 * 9620
# else :
#     급여 = 근무시간 * 9620 * 1.5
#
# 근무타입문자열 = 근무타입 == 1 and "주간" or "야간"
# print(f"{근무시간} 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.")


# 3번 문제 : 문자열 추가하기
# 2개의 문자열을 변수 s와 k에
# 양의 정수를 정수형 변수 n에 각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# s : seoul
# k : korea
# n : 2
# 결과 : ulkorea

s = input("s 문자열 : ")
k = input("k 문자열 : ")
n = int(input("정수 입력 : "))
print(s[len(s)-n:] + k)