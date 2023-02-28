# 1 ~ 1000 까지의 숫자중에 3이 들어있는 모든 수를 찾습니다.

answer = [number for number in range(1, 1000) if '3' in str(number)] 

print(answer)

# [x for x in range(1, 1001) if '3' in str(x)]

# * 문자열을 사용하지 않는 방법도 생각해보세요.


