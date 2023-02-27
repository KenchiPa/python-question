# 1 ~ 1000 까지의 숫자중에 3이 들어있는 모든 수를 찾습니다.

answer = [number for number in range(1, 1000) if '3' in str(number)] 

print(answer)