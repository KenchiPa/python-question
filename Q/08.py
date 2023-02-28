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


import random
# random 모듈에서 sample(컬렉션, 샘플수) 함수는 지정된 컬렉션으로부터 샘플수만큼 랜덤 추출을 한다.
numbers = random.sample(range(20), random.randint(1, 10))

answer2 = [('even' if x % 2 == 0 else 'odd') for x in numbers]
print(answer2)

answer3 = [['even', 'odd'][x % 2] for x in numbers]
print(answer3)
# * numbers 생성하려고 random 모듈 사용했는데 알면 좋은 거고 몰라도 되는 거고.
# list comprehension에서 조건식의 괄호는 식별하기 편하라고 넣은 것임


