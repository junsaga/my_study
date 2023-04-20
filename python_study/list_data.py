# #리스트(list) 자료형
# #여러개의 값을 변수 1개에 저장
# [1,2,3,4,5,6,7,8,9]
# [1,1,1,1,1]
# ["Hello","World","Python"]
# [1,"Hello",2,"WOW"]
# [1,2,["Hello","World"]]
# []


# li_1=[1,2,3]
# # print(li_1[0])
# # print(li_1[1])
# # print(li_1[2])
# print(li_1[-1])
# print(li_1[0]+li_1[1])

# li_2 =[1,2,3,[4,5,6]]
# print(li_2[3][0])
# print(li_2[2:3])
# print(li_2[1:])
# print(li_2[:2])
# print(li_2[3][0:2])
# print(li_2[0:1])
# print(li_2[0])
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# li_3 =[1,2,3,4,5,6]
# #출력 결과가 [2,3]이 되도록 만드세요.

# #[10,2,3,4,5]
# li_3[0]=10
# print(li_3)

# # append()
# # 리스트의 마지막에 원소를 추가
# li_4 =[1,2,3]
# li_4.append(4)
# li_4.append("문자")
# li_4.append([1,2,3])
# print(li_4)


#insert(원소,인덱스)
#인덱스 위치에 원소 삽입

li =[1,2,3]
li.insert(1,10)
print(li)
# li.remove(2) 
# print(li)
# li.remove(10)
# print(li)


# remove(값)
# 리스트에서 함수에 입력된 값과 같은 값을 찾아 삭제함

# pop(인덱스)
# 리스트의 인덱스 위치의 요소를 꺼낸다
# 인덱스를 함수에 전달하지 않으면 제일 마지막 요소를 꺼낸다.
# li=[1,2,3,4]
# a=li.pop()
# print(a) #[1,2,3]
# b=li.pop(1)
# print(li) #[1,3]
# print(b)

#index(값)
#리스트에서 값을 찾아 그 값의 인덱스를 돌려준다
#값이 리스트에 없으면 에러

# li =[1,2,3]
# idx=li.index(2) #1
# print(idx) #1
# #li[2] -----> 인덱싱(인덱스로 값에 접근)
# #li.index(값) -----> 인덱스 알아내기

# sort()
#리스트의 요소를 정렬한다
# li =[5,3,1,4,2]

# li.sort(reversed==True)
# print(li)


# reverse()
# 리스트의 순서를 뒤집는 함수
# # 정렬 아님
# li =[5,1,3,4,2]
# li.reverse()
# print(li) # [2,3,4,1,5]

# count(값)
# 리스트 안에서 해당 값이 몇 개 있는지 세고 개수를 돌려준다
# li =[1,2,3,2]
# cnt = li.count(2)
# print(cnt) #2



# # + 연산자
# # 리스트를 연결한다
# li_1 =[1,2,3]
# li_2 =[4,5,6]
# print(li_1+li_2)
# li_1.extend(li_2)

# *연산자
# 리스트를 반복한다
li=[1,2,3]
print(li*3) #[1,2,3,1,2,3,1,2,3]                                                                                          