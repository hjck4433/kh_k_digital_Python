# 배수 찾기
# 3
# 1
# 7
# 99
# 321
# 777
# 0
# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.

# n = int(input())
# ls = []
# while True :
#     num = int(input())
#     if num == 0 : break
#     ls.append(num)
#
# for e in ls :
#     is_multiple = f"is NOT a multiple of {n}.", f"is a multiple of {n}."
#     if e % n == 0 : print(e,is_multiple[1])
#     else : print(e,is_multiple[0])

## teacher
n = int(input()) # 문자열로 반환되기 때문에 정수타입으로 변환
ls = [] # 빈 리스트 생성
while True : # 0 입력 되기 전까지 반복 수행
    x = int(input()) # 목록의 수를 입력 받음
    if x == 0 : break # 0이 입력되면 탈출
    ls.append(x)

for e in ls :
    if e % n == 0 : print(f"{e} is a multiple of {n}.")
    else : print(f"{e} is NOT a multiple of {n}.")

# 피타고라스 정리 (중급)
# 피타고라스의 정리 : 직각삼각형에서 빗변을 제외한 나머지 두 변의 길이를
# 각각 제곱에 더하면 빗변의 길이의 제곱과 같다.
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# 6 8 10
# 10 8 6
# 25 52 60
# 5 12 13
# 0 0 0
# right
# right
# wrong
# right

# is_pytha = []
# while True :
#     tri = list(map(int,input().split()))
#     if tri[0] == 0 and tri[1] == 0 and tri[2] == 0 : break
# 
#     max_num = tri.pop(tri.index(max(tri)))
#     if (tri[0] ** 2) + (tri[1] ** 2) == max_num ** 2 :
#         is_pytha.append("right")
#     else : is_pytha.append("wrong")
#     # if (max(tri) ** 2) * 2 == (tri[0] ** 2) + (tri[1] ** 2) + (tri[2] ** 2) :
#     #     is_pytha.append("right")
#     # else : is_pytha.append("wrong")
# 
# for e in is_pytha : print(e)


## teacher
rst = [] # 결과를 출력하기 위한 빈 리스트
while True :
    li = list(map(int,input().split()))
    ls.sort()
    if li[0] == 0 and li[1] == 0 and li[2] == 0 : break
    elif li[0] ** 2 + li[1] ** 2 == li[2] ** 2 : rst.append("right")
    else : rst.append("wrong")

for e in rst : print(e)