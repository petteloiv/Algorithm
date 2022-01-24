# 국어, 수학 점수 튜플로 저장
# 이 튜플을 항목으로 갖는 리스트 객체

# trial 1

# scores = [(90, 80), (85, 75), (90, 100)]

# def print_score(scores):
#     total = 0
#     mean = 0
#     for i in scores:
#         for j in i:
#             total += j
#             mean = total/2
#             return f"{scores.index(i)}번 학생의 총점은 {total}점이고, 평균은 {mean}입니다." 

# print(print_score(scores))

# trial 2 

scores = [(90, 80), (85, 75), (90, 100)]

# def print_score(scores):
#     num = 0
#     total = 0
#     mean = 0
#     # 반복을 돌아야하는데 왜 반복을 안돌지 ㅠㅠㅠㅠ 
#     for i in scores:
#         num += 1
#         for j in i:
#             total += j
#         mean = total/2
#         return f"{num}번 학생의 총점은 {total}점이고, 평균은 {mean}입니다."

# cheatted code 1 

for i in scores:
    print("%d번 학생의 총점은 %d점이고, 평균은 %.1f입니다." % (scores.index(i)+1, sum(i), sum(i)/2))

# 복잡하게 함수로 만들 필요 없었다. 

# trial 3 

for i in scores: 
    print(f"{scores.index(i)+1}번 학생의 총점은 {sum(i)}점이고, 평균은 {sum(i)/len(i)}입니다.")