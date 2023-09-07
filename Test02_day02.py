# 1번 문제 : 세자리 정수를 입력 받은후 가장 큰 수 찾기 (123 => 3)
num = input("정수 입력 : ")
if int(num[0]) > int(num[1]) :
    rst = (int(num[0]) > int(num[2])) and int(num[0]) or int(num[2])
else :
    rst = (int(num[1]) > int(num[2])) and int(num[1]) or int(num[2])

print(rst)

# 2번 문제 : 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원
# 야간 근무 : 주간 시급 * 1.5
# 주간근무 [1] 야간근무[2]를 입력 하세요 :
# 근무 시간을 입력해 주세요
# 입력한 시간 동안 근무한 주간 또는 야간 급여는 ____원 입니다.
sel_work = int(input("[1]주간근무 [2]야간근무를 입력 하세요 : "))
time = int(input("근무 시간을 입력해 주세요 : "))
payroll = 9620 * time
if sel_work == 1 :
    print(f"{time}시간 동안 근무한 주간 급여는 {payroll}원 입니다.")
else :
    print(f"{time}시간 동안 근무한 야간 급여는 {payroll * 1.5:.0f}원 입니다.")


# 3번 문제 : 문자열 추가하기
# 2개의 문자열을 변수 s와 k에
# 양의 정수를 정수형 변수 n에 각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# s : seoul
# k : korea
# n : 2
# 결과 : ulkorea

s = input("문자 : ")
k = input("문자 : ")
n = int(input("정수 : "))

print(s[-n:] + k)
