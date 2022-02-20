
# 총 학생 수
T = int(input())
# 학생들이 뽑은 순서
students = list(map(int, input().split()))

# 뽑은 순서대로 정렬할 새 리스트
line_students = []

for i in range(T):
    # 학생 번호 집어넣을 인덱스
    np = i - students[i]
    # np 위치에 학생 번호 i (0부터 순회해서 +1 해준다..!)
    line_students.insert(np, i+1)

# 형식 맞춰서 출력
result = ' '.join(map(str,line_students))
print(result)

# print(line_students)