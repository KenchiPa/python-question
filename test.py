num = 3
total = 12

def solution(num, total):
    # num: 연속해서 더할 갯수
    # total: num개를 연속해서 더한 값
    # 정수배열을 오름차순으로 return
    
    max = (total + num) / num

    l = [int(max-x+1) for x in range(0, num)]
    l.sort()
    print(l)
    
    

solution(num, total)


# result: 1