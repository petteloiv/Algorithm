import sys
sys.stdin=open('input.txt')

password = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    bit = list(input() for _ in range(N))
    print(bit)

    # 뒤에서 1 찾기
    for i in range(len(bit) - 1, -1, -1):
        if bit[i] == '1':
            point = i
            break
    # print(point)
    # 최종 출력 값
    result = ''
    while point - 6 > 0:
        if bit[point - 5:point + 1] in password:
            # 뒤에서부터 조사중임
            # 뒷 번호부터 더해 나가려면 => 최종 0 2 / 내가 가진 값 2
            result = ' ' + str(password[bit[point - 5:point + 1]]) + result
            # print(password[bit[point-5:point+1]], end= '')
            point -= 6
        else:
            # 못찾으면 다음칸으로 이동 ..
            point -= 1

    # print(result)
    print(result.lstrip())

