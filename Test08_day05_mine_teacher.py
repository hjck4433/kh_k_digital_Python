# A = 1000 , B = 70  => 1대 1,070 / 10대 1,700
# C = 책정 가격

# 첫째 줄에 A,B,C가 빈 칸을 사이에 두고 순서대로 준어진다. A,B,C는 21억 이하의 자연수이다
# 출력: 첫 째 줄에 손익분기점 즉 최초로 이익이 발생하는 판매량 출력/ 손익분기저밍 존재하지 않으면 -1
# 1000 70 170 => 11  /  3 2 1 => -1  / 2100000000 9 10 => 2,100,000,001
A, B, C = map(int, input().split())
# if A // (C - B) > 0 :
#     print(A // (C - B) + 1)
# else : print(-1)

if B >= C :
    print(-1)
else :
    print(A // (C - B) + 1)

# teacher
# 고정비용 : 1000
# 가변비용 : 70
# 판매비용 : 170
fix, var, sell = map(int,input().split())
# cnt = 0
# while True :
#     #if fix + (var * cnt) < sell * cnt :  break
#     if cnt>fix // (sell-var) : break
#     cnt += 1
#
# if sell <= var : print(-1)
# else : print(cnt)

# 방법 2
if sell <= var : print(-1)
else: print(fix // (sell-var) + 1)


