# N명의 참가자 -> 1번 ~ N번
# 서로 인접한 번호끼리 스타 -> 이긴 사람 다음 라운드 진출
# 참가자 홀수 => 마지막 참가자 다음 라운드 자동 진출
# 처음 번호 순서 유지하면서 다시 1번부터
# 1명만 남을때까지 유지
# 둘은 항상 이긴다고 가정
# 몇라운드에서 대결하는지 출력

n, j, h = map(int, input().split())

cnt = 0

while j != h :
    j -= j//2
    h -= h//2
    cnt += 1

print(cnt)