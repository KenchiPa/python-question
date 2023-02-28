# 다음 목록에서 일치하는 숫자로만 구성된 튜플 목록을 생성합니다. 
# list_a = 1,2,3,4,5,6,7,8,9, list_b = 2,7,1,12. 결과는 (2,2), (7,7) 처럼 표시합니다..

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
 
for x in list_a:
    if x in list_b:
        list=[]
        list.append(x)
        list.append(x)
        print(tuple(list))

list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12]

temp = [(x, y) for x in list_a for y in list_b]
print("temp", temp)
answer3 = [(x, x) for x in list_a if x in list_b]
print("answer3", answer3)

# * in 연산자를 사용해도 내부적으로는 반복적으로 처리한다는 걸 생각해야 합니다.
#   대신 명시적인 반복문보다는 in 연산자가 더 빠를 가능성이 높습니다.

#    원래는 동일 값을 검색하는게 아니고 동일 값이 위치하는 인덱스를 표시하는 걸 생각했습니다.
#    [(0, 2), (1, 0), (6, 1)]
;
