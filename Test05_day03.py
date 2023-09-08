# 1번 : 상근날드, 초급에서 검색
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류
menu = []
for i in range(5):
    while True :
        price = int(input())
        if 100 <= price <= 2000:
            menu.append(price)
            break
        print("가격 설정 가능 범위를 벗어났습니다")
burger = menu[:3]
drink = menu[3:]
set_price = []
for i in range(len(burger)) :
    for e in range(len(drink)):
        set_price.append(burger[i] + drink[e] - 50)
print(min(set_price))

# 2번 : 저항, 중급에서 검색
# colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# color = []
# for i in range(3) :
#     color.append(input())
#
# rst = ((colors.index(color[0])*10) + colors.index(color[1])) * (10 ** colors.index(color[2]))
# print(rst)

# 3번 : PC방 알바, 중급에서 검색
n = int(input())
seat = []
for i in range(n) :
    while True :
        sel = int(input())
        if 0 < sel <= 100:
            if sel not in seat:
                seat.append(sel)
            break
        print("없는 좌석 입니다")

print(n-len(seat))

# 4번 : Knuth-Morris-Pratt => KMP, Mirko-Slavko = MS
# name = input().split("-")
# for e in name :
#     print(e[0],end="")