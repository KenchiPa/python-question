# "hi", 4, 8.99, 'apple', ('t,b','n') 목록의 항목에 대한 인덱스와 값을 튜플 형태로 가져옵니다. 결과는 (인덱스, 값), (인덱스, 값)과 같이 표시됩니다.

a = ["hi", 4, 8.99, 'apple', ('t,b','n')]

answer = [item for item in enumerate(a)]

print("answer", answer)

list2 = ["hi", 4, 8.99, 'apple', ('t,b','n')]
answer2 = list(enumerate(list2))
print("answer2", answer2)

