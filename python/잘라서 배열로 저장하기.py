# 잘라서 배열로 저장하기 - 프로그래머스

import math


my_str = "abc1Addfggg4556b"
n = 6


def solution(my_str, n):
    # my_str: 문자열
    # n: 길이 
    # my_str을 길이 n씩 잘라서 저장한 배열을 return
    
    answer = []
    str = list(my_str)
    str.reverse()
    print("역정렬: ", str)

    for y in range(math.ceil(len(str)/n)):
        temp = []
        print('반복')
        for x in range(n):
            try:
                temp += str.pop()
                temp = ''.join(temp)
                print("temp: ", temp)
            except:
                break
        answer.append(temp)
    print(answer)
    return answer


solution(my_str, n)

####################################################################################################################
# 이상적인 답안

# my_str = "abc1Addfggg4556b"
# n = 6
# 2
# 3
# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]

# solution(my_str, n)