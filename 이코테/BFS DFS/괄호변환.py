# 균형잡힌 괄호 문자열 : 개수 같음
# 올바른 괄호 문자열 : 개수 + 짝
# 균형 -> 올바른 변환 과정 :
# 1) 빈 문자열 -> 빈 문자열
# 2) u (균형 / 더 이상 분리 XX ) & v (빈 문자열 가능)
# 3) 수행 결과를 u + ' 문자열 ' return
# 4) if u가 올바른 아니면 다시 수행
# 1. 빈 문자열 + (
# 2. vㅔ 대해 1) 부터 수행한 결과 문자열 붙이기
# 3. ) 붙이기
# 4. 첫번째 마지막 제거


def solution(w):
    ans = ''

    # 빈 문자열일 때
    if not w:
        return ''

    # 냅다 나누기
    u, v = divide(w)

    # 균형 체크
    if balance(u):
        return u + solution(v)
    else:
        ans = '('
        ans += solution(v)
        ans += ')'

        for p in u[1:len(u) - 1]:
            if p == '(':
                ans += ')'
            else:
                ans += '('

    return ans

# 문자열 나누기
def divide(w):
    # 더 이상 안나눠지는 균형잡힌 문자열
    open, close = 0,0
    for i in range(len(w)):
        if w[i] == '(':
            open += 1
        else:
            close += 1

        if open == close :
            return w[:i+1], w[i+1:]

def balance(u):
    stack = []
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True