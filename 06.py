# (튜플이나 집합을 사용하지 않고) 두 목록에서 공통된 숫자 찾기 list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5


list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

answer = [x for x in list_a if x in list_b]
print(answer)