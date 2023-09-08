# 예제 설명 : 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제 입니다.
# 기본
num = list(map(int,input("입력 : ").split()))
# even = []
# odd = []
# for e in num :
#     if e % 2 == 0 : even.append(e)
#     else: odd.append(e)
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")

# map : 전달 받은 갯수를 함수내부에서 가공해서 반환 (입력 개수와 반환 개수가 동일)
# filter : 전달 받은 값을 함수내부에서 조건에 일치하는 것만 골라서 반환

# 람다식 방법
odd = list(filter(lambda e: int(e) % 2 == 1,num))
even = list(filter(lambda e: int(e) % 2 == 0,num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")