# 회원정보 출력하기 (1단계는 현재 상태대로 -> 함수 형태로)
# 이름/ 나이/ 성별/ 직업 / 결과 출력
# cnt = 0 #회원정보 입력 횟수
# def input_age() :
#     while True :
#         age = input("나이를 입력 하세요 : ")
#         if age.isdigit():  # 문자열이 숫자로 구성되어 있는지 확인
#             age = int(age)
#             if 0 < age < 200: return age
#         print("나이를 잘 못 입력 하셨습니다.")
#
# def input_gender() :
#     while True:
#         gender = input("성별을 입력 하세요 : ")
#         if gender == 'M' or gender == 'm' : return "남성"
#         elif gender == 'F' or gender == "f" : return "여성"
#         print("성별을 잘 못 입력 되었습니다.")
#
# def input_jobs() :
#     while True:
#         jobs = input("직업을 입력 하세요 1(학생), 2(회사원), 3(주부), 4(무직) : ")
#         if jobs.isdigit():
#             jobs = int(jobs)
#             if 0 < jobs < 5: return jobs
#         print("직업을 잘 못 입력 하셨습니다.")
#
# def print_info(name, age, gender, jobs, cnt) :
#     jobs_str = "", "학생", "회사원", "주부", "무직"
#     print("=" * 3, "회원정보", "=" * 3)
#     return "=" * 3 + "회원정보" + str(cnt) + "=" * 3 + "\n" + f"이름 : {name} \n 나이 : {age} \n성별 : {gender} \n직업 : {jobs_str[jobs]} \n"
#     # print(f"이름 : {name} \n 나이 : {age} \n성별 : {gender} \n직업 : {jobs_str[jobs]}")
# # 함수는 선언 이후 호출해야 동작 함.
# member_info = "Test03_member.txt"
# fd = open(member_info, "wt", encoding="UTF8")
# # str = "=" * 3 + "회원정보" + "=" * 3+"\n" # 회원정보 제목 한번만 맨 위에 표시하고 싶을때
# # fd.write(str)
# while True :
#     cnt += 1
#     name = input("이름을 입력 하세요 (종료하려면 quit)): ")
#     if name == "quit" : break
#     age = input_age()
#     gender = input_gender()
#     jobs = input_jobs()
#     #print_info(name, age, gender, jobs)
#     rst = print_info(name, age, gender, jobs,cnt)
#     fd.write(rst)
# fd.close()


#name = input("이름을 입력 하세요: ")
# while True :
#     age = input("나이를 입력 하세요 : ")
#     if age.isdigit() : # 문자열이 숫자로 구성되어 있는지 확인
#         age = int(age)
#         if 0 < age < 200 : break
#     print("나이를 잘 못 입력 하셨습니다.")

# while True :
#     gender = input("성별을 입력 하세요 : ")
#     if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f' : break
#     print("성별을 잘 못 입력 되었습니다.")

# while True :
#     jobs = input("직업을 입력 하세요 1(학생), 2(회사원), 3(주부), 4(무직) : ")
#     if jobs.isdigit() :
#         jobs = int(jobs)
#         if 0 < jobs < 5 : break
#     print("직업을 잘 못 입력 하셨습니다.")

# if gender == 'M' or gender == 'm' : gen_str = "남성"
# else : gen_str = "여성"

# jobs_str = "" ,"학생" ,"회사원" ,"주부" ,"무직" # 튜플로 인식 / 내용 변경 불가

# print("="*3, "회원정보", "="*3)
# print(f"""이름 : {name}
# 나이 : {age}
# 성별 : {gen_str}
# 직업 : {jobs_str[jobs]}
# """)



# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원
# n = int(input()) #통화 횟수
# call = list(map(int, input().split())) # 통화 횟수에 대한 통화 시간
#
# y_pay = m_pay = 0
#
# for i in range(n) :
#     y_pay += call[i] // 30 * 10 + 10
#     m_pay += call[i] // 60 * 15 + 15
# if y_pay > m_pay :
#     print("M", m_pay)
# elif y_pay < m_pay :
#     print("Y", y_pay)
# else:
#     print("Y M", y_pay)


#대소문자 바꾸기
# 영어 소문자와 대문자로 이루어진 단어를 입력 받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오
# rst = ""
# for e in input(): # 입력 받는 문자열만큼 자동순회
#     if e.islower() :
#         rst += e.upper()
#     else :
#         rst += e.lower()
# print(rst)

# for e in input(): # 입력 받는 문자열만큼 자동순회
#     if e.islower() : print(e.upper(), end="")
#     else : print(e.lower(), end="")


# 숫자의 개수
# A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300
# 0부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력
a, b, c = map(int,input("정수 3개 입력 : ").split())
total_val = str(a * b * c) # a * b * c 결과를 문자열 변환
for i in range(10) :
    print(total_val.count(str(i)))





