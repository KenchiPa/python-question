# numbers(in range(20))가 주어졌을 때, 
# 숫자의 숫자가 짝수이면 'even', 홀수이면 'odd'라는 단어가 포함된 목록을 생성합니다. 결과는 'odd', 'odd', 'even' 처럼 표시합니다.

input_count = input("입력할 숫자의 갯수를 입력하세요 >>> ")
input_range = 0
number = []
answer = []




for cnt in range(1,int(input_count) + 1):
    print(type(cnt))
    c = input(f'{cnt}번째 숫자를 입력해주세요')
    if 0 <= int(c) < 20:
        number.append(int(c))
print(number)
for num in number:
    if num % 2 == 0:
        answer.append("even")
    else:
        answer.append("odd")   
print(answer)    
