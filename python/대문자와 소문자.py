# 대문자와 소문자 - 프로그래머스

my_string = "abCdEfghIJ"

def solution(my_string):
    temp =[]
    for x in my_string:
        print(x)
        if x.isupper():
            x = x.lower()
            temp += x
        else:
            x = x.upper()
            temp += x 
    print(temp)
    temp = ''.join(temp)
    print(temp)
    return temp


solution(my_string)

# 기댓값: "ABcDeFGHij"
####################################################################################################################
# 이상적인 답안

# my_string = "abCdEfghIJ"

# 1
# def solution(my_string):
#     return my_string.swapcase() 

# 2
# def solution(my_string):
#     return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])