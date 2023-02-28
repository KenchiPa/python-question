# 집합 자료형의 특징
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered)

s1 = set([1, 2, 3])
print(type(s1))
print(s1)

s2 = set("Hello")
print(s2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
# 합집합
print(s1 | s2)
# 차집합
print(s1 - s2)


# 집합 자료형 관련 함수들
s1 = set([1, 2, 3])
s1.add(4)  # 값 1개 추가하기
print("s1", s1)
s1.update([4, 5, 6])  # 값 여러 개 추가하기
print(s1)
s1.remove(6)  # 특정 값 제거하기
print(s1)