# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음
# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함

# 큰값 작은값 찾기
print(max(23,45,67,200,30,40,44,77,88,100))
print(min(23,45,67,200,30,40,44,77,88,100))

# 총 합 구하기
print(sum([23,45,67,200,30,40,44,77,88,100])) # 리스트에 대한 총 합
print(sum((23,45,67,200,30,40,44,77,88,100))) # 튜플에 대한 총 합
# num = list(map(int,input("정수값 입력 : ").split()))
# print(f"입력 받은 수의 총 합 : {sum(num)}")
# print(f"입력 받은 수의 평균 : {sum(num)/len(num) : .2f}")

# 몫과 나머지 구하기
print(f"몫과 나머지 : {divmod(10, 4)}") # 튜플의 동작 원리, 두개의 반환값으로 받음

# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균, 몫과 나머지

# nums = list(map(int,input("정수 입력 : ").split()))
# nums_divmod = divmod (sum(nums),5)
# print(f"""최대값 : {max(nums)}
# 최소값 : {min(nums)}
# 합계 : {sum(nums)}
# 평균 : {sum(nums) / len(nums):.2f}
# 몫 : {divmod (sum(nums),5)[0]}, 나머지 : {nums_divmod[1]}
# """)

# 정렬
my_list = [23,45,67,200,30,40,44,77,88,100]
print(sorted(my_list)) #오름 차순
print(sorted(my_list, reverse = True)) #내림 차순


