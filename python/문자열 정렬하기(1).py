# 문자열 정렬하기(1) - 프로그래머스

my_string = "p2o4i8gj2"

def solution(my_string):
    a = [int(x) for x in my_string if x.isdigit()].
    a.sort()
    print(a)


solution(my_string)

# 기댓값: [2, 2, 4, 8]
####################################################################################################################
# 이상적인 답안

# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()])


