# 테스트 케이스 개수 C
# 둘째 ~ C번 줄 학생 수 N , 학생 수 만큼의 점수

# def input_score():
#     score = list(map(int, input().split()))
#     return score
#
#
# def avg_student(score):
#     avg = sum(score[1:]) / score[0]
#     cnt = 0
#     for i in range(1, len(score)):
#         if score[i] > avg: cnt += 1
#     return cnt / score[0] * 100
#
#
# c = int(input())
# avg_list = []
# while True:
#     avg_list.append(avg_student(input_score()))
#     c -= 1
#     if c == 0: break
#
# for e in avg_list:
#     print(f"{e:.3f}%")

# c = int(input())
# case_list = []
# for i in range(c):
#     case_list.append(list(map(int,input().split())))
#
# for i in case_list :
#     avg = sum(i[1:]) / i[0]
#     cnt = 0
#     for e in range(1,len(i)) :
#         if i[e] > avg : cnt+=1
#     print(f"{cnt / i[0] * 100 :.3f}%")

c = int(input())
avg_list = []
for i in range(c):
    case_list = list(map(int,input().split()))
    n = case_list.pop(0)
    case_list = list(filter(lambda s: s > sum(case_list)/n, case_list))
    avg_list.append(len(case_list) / n * 100)

for a in avg_list: print(f"{a:.3f}%")