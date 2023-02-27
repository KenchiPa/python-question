# "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"라는 문자열에 있는 모든 자음의 목록을 만듭니다.
# 영어에서의 모음은 a, e, i, o, u 이다.
b = ['a', 'e', 'i', 'o', 'u']

string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
a = list(set(string))  # 중복 글자 제거
print(a)

a = ' '.join(a).split()
print(a)

answer = [i for i in a if i not in b]

print(answer)

