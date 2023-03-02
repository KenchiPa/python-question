# 대문자와 소문자 - 프로그래머스

cipher = "dfjardstddetckdaccccdegk"
code = 4


def solution(cipher, code):

    a = cipher[code-1:len(cipher):code]
    print(a)
    return a


solution(cipher, code)

# 기댓값: "attack"
####################################################################################################################
# 이상적인 답안


# def solution(cipher, code):

#     return cipher[code-1::code]