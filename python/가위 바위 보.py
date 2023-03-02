# 가위 바위 보 - 프로그래머스


rsp = "205"

def solution(rsp):
    # 가위: 2
    # 바위: 0
    # 보: 5
    # rsp: 가위 바위 보를 내는 순서대로 나타낸 문자열
    # 모두 이기는 경우를 순서대로 나타낸 문자열을 return
    # rsp = list(rsp)
    # print("rsp", rsp)
    temp1 = []
    
    for x in rsp:
        
        if int(x) == 0:
            temp1.append("5")
            print("5 추가")
        elif int(x) == 2:
            temp1.append("0")
            print("0 추가")
        elif int(x) == 5:
            temp1.append("2")
            print("2 추가")
    print("반복문 탈출")
    print(type(temp1))
    answer = ''.join(temp1)
    return answer

solution(rsp)

# 기댓값: "052"
####################################################################################################################
# 이상적인 답안
4
# rsp = "205"

# def solution(rsp):
#     d = {'0':'5','2':'0','5':'2'}
#     return ''.join(d[i] for i in rsp)

# solution(rsp)