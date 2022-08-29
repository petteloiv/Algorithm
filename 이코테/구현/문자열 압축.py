# 같은 값이 연속해서 나타나는 것을 그 문자의 개수 & 반복되는 값으로 표현
# 더 짧은 문자열로 줄여서 표현하는 알고리즘 공뷰
# 한번만 나타난 경우 1은 생략
# ex) aabbaccc = 2a2ba3c
# 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지?!
# 몇 개 단위로 압축해야 가장 짧은지 ... 가장 짧은 것의 길이 return
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야한다!!!!!!!!!!!!!

# 그냥 앞에서부터 ... 1부터 문자열길이만큼 다 체크하면 안될까?

def solution(s):
    length = []
    result = ""

    # 문자열 길이가 1이면 그냥 1 return
    if len(s) == 1:
        return 1

    # 자를 수 있는 최대 길이 -> 문자열 절반!
    for cut in range(1, len(s) // 2 + 1):
        count = 1
        # 현재 자른 단위..
        now = s[:cut]

        # 앞에서부터 자르니까 ,, cut 이후부터 cut만큼 건너뛰면서 확인
        for i in range(cut, len(s), cut):
            # 다음 cut번째가 같다면 일치 카운트 + 1
            if s[i:i + cut] == now:
                count += 1
            # 다르다면,, 카운트 초기화 & 새 문자열에 더해주기
            else:
                if count == 1:
                    count = ""
                result += str(count) + now
                # 자른 문자열(?) 변경 i:i+cut
                now = s[i:i + cut]
                count = 1

        # 1개 단위는 숫자 표시 안함
        if count == 1:
            count = ""
        result += str(count) + now
        length.append(len(result))
        result = ""

    return min(length)

# ---------------------------------------------------------
def solution(s):

    result = []

    n = len(s)

    if n == 1:
        return 1

    for i in range(1, (n//2)+1):

        # 단어 리스트로 변환해서 알파벳 하나하나...
        word = list(s)

        # 체크할 때마다 초기화
        newword = ''
        before = ''
        now = ''

        samealpha = []
        sameletter = ''

        # 초기값 (맨 앞 글자)
        for j in range(i):
            now += word.pop(0)

        while True:
            next = ''
            if now == '':
                result.append(len(newword))
                break

            # word 리스트에 있는 알파벳들이 단위보다 많거나 같으면
            # 더 확인할 수 있음
            if len(word) >= i:
                next += word.pop(0)

            # 단위보다 작지만 문자 남아 있을 때
            elif len(word) < i and word:
                # 없을때까지 빼서 추가하기..
                while word:
                    next += word.pop(0)

            # 리스트 비어있으면 초기화...
            elif not word:
                next = ''

            # 연속될 때
            if before == now or now == next:
                samealpha.append(now)
                samealpha = now
            else:
                newword += now

            # 연속되는 원소 끝날 때
            if samealpha and now != next:

                # 새 단어에 자른단어(?) 개수 + 단어로 새로 입력
                cnt = samealpha.count(sameletter)
                newword += str(cnt) + sameletter

                # 초기화
                samealpha = []
                sameletter = ''

            # 다음으로 이동,,,
            before = now
            now = next

    return min(result)





# ---------------------------------------------------------

def solution(s):
    answer = 10000000000000
    n = len(s)

    for i in range(1,n//2+1):
        result = ''
        cnt = 1
        now = s[:n]

        for j in range(i, n+i, i):
            if now == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    result += now
                else:
                    result += str(cnt)+now
                now=s[j:j+i]
                cnt = 1
        ans = min(answer, len(result))
    return ans

