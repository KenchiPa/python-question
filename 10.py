# 문자열에서 4글자보다 작은 단어 모두 찾기
sentence = '문자열에서 4글자보다 작은 단어 모두 찾기'

a = sentence.split()
answer = [x for x in a if len(x)<4]

print(answer)