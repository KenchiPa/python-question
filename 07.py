# 'In 1984 there were 13 instances of a protest with over 1000 people attending'와 같은 문장에서 숫자만 구합니다.

sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending"
answer = []
for item in sentence:
    try:
        int(item)
        answer.append(item)
    except:
        continue

print(answer)