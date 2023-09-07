# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초
# time = input("시간 입력 : ").split(":")
# hour = int(time[0])
# time_min = int(time[1])
# sec = int(time[2])
#
# if hour > 12:
#     hour -= 12
#     print(f"오후 {hour}시 {time_min:02}분 {sec:02}초")
# else:
#     print(f"오전 {hour}시 {time_min:02}분 {sec:02}초")
from datetime import datetime

# 2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
# num1, num2, num3 = map(int,input("정수 입력 : ").split())
# max_num = 0
# min_num = 0
# if num1 > num2 and num1 > num3 :
#     max_num = num1
#     if num2 > num3:
#         min_num = num3
#     else:
#         min_num = num2
# elif num2 > num1 and num2> num3 :
#     max_num = num2
#     if num3 > num1:
#         min_num = num1
#     else:
#         min_num = num3
# else :
#     max_num = num3
#     if num1 > num2:
#         min_num = num2
#     else:
#         min_num = num1
#
# print(f"최대값 : {max_num} , 최소값 : {min_num}")

# 3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# current_year = datetime.today().year
# social_num = input("주민번호 : ")
# birth_date = social_num[:6]
# gender = social_num[7]
# year = int(birth_date[:2])
# if birth_date[0] == 0:
#     year += 2000
# else:
#     year += 1900
# current_year = datetime.today().year
# age = current_year - year
#
# print("생년월일 : " + str(birth_date))
# if gender == "1" and gender == "3:
#     print("성별 : 남성")
# else:
#     print("성별 : 여성")
# print("나이 : " + str(age))

# 4. 개수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기
input_nums = list(input("숫자입력 : ").split())
#print(input_nums)
sum = 0
cnt = 0
list_len = len(input_nums)
# while True:
#     sum += int(input_nums[cnt])
#     cnt += 1
#     if cnt == list_len: break

# for n in input_nums:
#     sum += int(n)

for i in range(0, len(input_nums)) :
    sum += int(input_nums[i])


avg = sum / list_len
print(f"합계 :{sum} , 평균 : {avg:.2f}")







