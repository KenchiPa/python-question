# "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"라는 문자열에 있는 모든 자음의 목록을 만듭니다.
# 영어에서의 모음은 a, e, i, o, u 이다.
b = ['a', 'e', 'i', 'o', 'u']

string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
a = list(set(string))  # 중복 글자 제거
print(a)

a = ' '.join(a).split()
print(a)

answer = [i for i in a if i not in b]
answer.sort()
print("answer", answer)  # 문제점 발견: 대소문자 구분되어 중복이 존재한다.


s = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

print([c.lower() for c in s if c.isalpha() and c.lower() not in 'aeiou'])

print("answer2", sorted(set([c.lower() for c in s if c.isalpha() and c.lower() not in 'aeiou'])))

# * sorted 안하고 list로 list로 변환을 해도 되지만, sort안하면 순서대로 나오지 않아서 값을 확인하기 쉽지 않으니까.

