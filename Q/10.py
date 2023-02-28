# 문자열에서 4글자보다 작은 단어 모두 찾기
sentence = '문자열에서 4글자보다 작은 단어 모두 찾기'

a = sentence.split()
answer = [x for x in a if len(x)<4]

print(answer)


# s = "Yellow Yaks like yelling and yawning and yesturday they yodled 
# while eating yuky yams"
# [x for x in s.split() if len(x) < 4]
