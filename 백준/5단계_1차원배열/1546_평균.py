# ----------- 문제 ------------# 
# 입력값
# 첫째줄 : 과목수 
# 둘째줄 : 시험 성적 

# 최댓값 M 고르고 
# 모든 점수 = 기존 점수/M*100 

# new 평균 .. 

# -----------풀이 ---------------# 

n = int(input())
score = list(map(int, input().split()))
m = max(score)

for i in range(len(score)):
    score[i] = score[i]/m*100

print(sum(score)/n)
