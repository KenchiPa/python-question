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