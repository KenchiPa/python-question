# 대문자와 소문자 - 프로그래머스

n = 2
t = 10


def solution(n, t):


    b =  n * 2**(t)
    print(b)
    return b


    # a = [n**(x+1) for x in range(n, t+1)]
    # print(a)
    # print(a[-1])

solution(n, t)

# 기댓값: "2048"
####################################################################################################################
# 이상적인 답안



# def solution(n, t):
#     return n << t