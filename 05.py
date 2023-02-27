# "hi", 4, 8.99, 'apple', ('t,b','n') 목록의 항목에 대한 인덱스와 값을 튜플 형태로 가져옵니다. 결과는 (인덱스, 값), (인덱스, 값)과 같이 표시됩니다.

list = ["hi", 4, 8.99, 'apple', ('t,b','n')]

answer = [item for item in enumerate(list)]

print(answer)