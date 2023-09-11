# 테스트 케이스 개수 C
# 둘째 ~ C번 줄 학생 수 N , 학생 수 만큼의 점수

def input_score () :
    score = list(map(int,input().split()))
    return score
def avg_score(score) :
    return sum(score[1:]) / score[0]

c = int(input())
avg_list = []
while True :
    avg_list.append(avg_score(input_score()))
    c -= 1
    if c == 0 : break

for e in avg_list :
    print(f"{e:.2f}%")



