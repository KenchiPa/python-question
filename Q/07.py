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

sentence2 = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
answer2 = [x for x in sentence2.split() if x.isdigit()]  # isdigit(): 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
                                                         # 문자가 '단 하나'라도 있다면 False를 반환하고,
                                                         # 모든 문자가 '숫자'로만 이루어져있으면 True를 반환한다.
print(answer2)


