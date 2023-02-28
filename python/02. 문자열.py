# 문자열 "", '', """ """, ''' '''
# 문자열 곱하기: 반복을 의미
# 문자열 길이 구하기 len()

a = "life is too short, you need python"

print(len(a))
print(a[1] + a[3])
print(a[1:3])
print(a[:3])
print(a[5:])
print(a[:])

# 문자열 포매팅
number = 3
day = "three"

print("I eat %d apples." %3)
print("I eat %s apples." %"five")
print("I eat %d apples. so I was sick for %s days" %(number, day))

a = " hello "
print(a.strip())
print(a.replace("h", "H"))

a = "Life is too short"
print(a)
print(a.split())  # split(): 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
print(a.split(' '))
a = "a,b,c,d"
print(a.split(','))