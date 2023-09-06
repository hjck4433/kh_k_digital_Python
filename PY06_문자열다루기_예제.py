# ***각 사이트 비밀번호 자동으로 만들기***
# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o' 갯수 +글자에 포함된 'k' 갯수+ '!' + 자신의이니셜(예: 'jks')

# 내 풀이
# site_addr = input("사이트 입력 : ")
# site_name = site_addr.replace("http://","")
# name = site_name.split(".")
# password = name[0][0:3] + str(len(name[0])) + str(name[0].count("o"))+str(name[0].count("k")) + "!" + "khj"
# print("비밀번호 : " + password)

# 강사님 풀이
file_name = "password.txt"
fd = open(file_name, "wt") # wt => write_text

while True:
    url = input("사이트 : ")
    if url == "exit": break
    my_str = url.replace("http://","")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱 : 처음부터 "." 인덱스 미만 까지
    password_t = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "khj"
    print("비밀번호 : " + password_t)
    fd.write(password_t + "\n")  # write 에는 줄바꿈 특성이 없기 때문에 "\n" 필요
fd.close()


