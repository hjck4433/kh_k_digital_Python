# 예제 설명 : 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제 입니다.

num_list = list(map(int,input("정수 입력 : ").split()))
# odd = []
# even = []
# for e in num_list :
#     if e % 2 == 0: even.append(e)
#     else : odd.append(e)
#print(f"홀수: {odd} \n 짝수 : {even}")

print(f"홀수 : {list(filter(lambda e: int(e) % 2 != 0,num_list))}")
print(f"짝수 : {list(filter(lambda e: int(e) % 2 == 0,num_list))}")

#print(f"""홀수 : {list(filter(lambda e: int(e) % 2 != 0,num_list))}
#짝수 : {list(filter(lambda e: int(e) % 2 == 0,num_list))}
#""")

# odd = list(filter(lambda e: int(e) % 2 != 0,num_list))
#even = list(filter(lambda e: int(e) % 2 == 0,num_list))
#print(f"홀수: {odd} \n 짝수 : {even}")

