# 리스트명 = [요소1, 요소2, 요소3, 요소4]

a = [1, 2, 3]
print(len(a))

# 리스트의 수정과 삭제
a = [1, 2, 3, 4]
a[2] = 9
print(a)
del a[2]
print(a)

a.append(5)  # 리스트에 추가
print(a)

a = [1, 5, 2, 7]
a.sort()  # 오름차순 정렬
print(a)
a.reverse()  # 뒤집기
print(a)

print(a.index(2))  # 숫자 2가위치한 인덱스 반환

a.insert(0, 0)  # insert(index, x): index위치에 x 삽입
print(a)

# 리스트 요소 제거(remove): 리스트에서 첫 번째로 나오는 x를 삭제하는 함수.
# 리스트 요소 끄집어내기(pop): 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.
# 리스트에 포함된 요소 x의 개수 세기(count): 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 리턴한다.
# 리스트 확장(extend): x에는 리스트만 올 수 있으며 원래의 a 리스트에 x리스트를 더하게 된다