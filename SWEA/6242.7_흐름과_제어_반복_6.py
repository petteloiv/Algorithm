# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

# for 문 사용
# 딕셔너리 형식 반환 

blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
student_blood_type = {'A':0, 'O':0, 'B':0, 'AB':0}

count_A = 0
count_B = 0
count_AB = 0
count_O = 0

for i in blood_type:
    if i == 'A':
        count_A += 1
        student_blood_type['A'] = count_A
    elif i == 'B':
        count_B += 1
        student_blood_type['B'] = count_B
    elif i == 'AB':
        count_AB += 1
        student_blood_type['AB'] = count_AB
    else:
        count_O += 1
        student_blood_type['O'] = count_O

print(student_blood_type)

# 처음에 딕셔너리에 값을 각각 집어넣는 식으로 해서 실행 안됨 .. 
# 딕셔너리 추가하는 방법을 잘못 알고있었다. 
# student_blood_tye = {'O': count_O }
# 이런식으로 집어넣었다. 

# 딕셔너리 추가 및 수정 방법 : 
# 딕셔너리이름['키값'] = 밸류