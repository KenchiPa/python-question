def solution(my_string):
    # my_string: 문자열
    # return my_string 거꾸로 뒤집은 문자열 
    result = []
    for char in my_string:
        result.insert(0 , char)
        print("list", result)
        a = str(result).split(',')
        print(a)


solution('abcdef')