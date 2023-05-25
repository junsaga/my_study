# a =[10,9,8,7,6]
# b=[5,7,8,9,10]
# print(id(a),id(b))
# b=a
# a.sort()
# print(b)


# a =[5,4,3,2,1]
# b=a[:]
# print(id(a),id(b))
# print(b)
# a.sort()
# print(a)
# print(b)

# a=10 
# b=10
# a==b
# print(a is b)

# a=300
# b=300

# a==b

# print(a is b)

# a=-5
# b=-5
# print(a is b)

# a=-6
# b=-6
# print(a is b)

# a =[1,2,3,4,5]
# b=a[:]

# print(a)
# print(b)
# print(a is b)

# import copy
# a =[1,2,3,4,5]
# b =copy.deepcopy(a)

# print(a)

# print(b)

# print(a is b)

# a = 100
# if a>0 and (a%2)==0:
#     print('a is even')

# print(5 and 7)
# print(7 and 13)

# # and 조건이 True/False로 반환이 됨
# # &: 비트 연산자로 작동됨

# print(7&13)
# print(13&7)

# a=100
# if a>0 or (a%2)==0:
#     print('a is even')

# print(5 or 7)
# print(7 or 13)

# # or : 조건이 True/False로 반횐이 됨
# # | : 비트연산자로 작동 됨

# print(7 | 13)
# print(13 | 7)
# print(34//4)
#b로 a를나눈 나머지가 3초과면 실패,3이면 무승부,3미만이면 성공이 출력되도록 만들어 보자
# a=34
# b=4
# if (b%a) >3:
#     print("실패")
# elif (b%a)==3:
#     print("무승부")
# elif (b%a)<3:
#     print("성공")


# 당신이 태어난 년도를 입력하세요
# -나이는 현재년도-태어난년도+1로 계산
# 26세 이하 20세 이상이면"대학생"20세미만 17세 이상이면 고등학생
# 17세 미만 14세 이상이면"중학생" 14세미만 8세 이상이면 초등학생
# 그 외의 경우는 학생이 아닙니다 출력

# birthyear = int(input("태어난 년도>"))
# age= 2023-(birthyear+1)
# if 26 >= age >=20:
#     print("대학생")
# elif 20>age>=17:
#     print("고등학생")
# elif 17>age>=14:
#     print("초등학생")
# else:
#     print('학생이 아닙니다')

# 양의 정수 하나를 입력 받아 이 정수가 2의 배수인지
# 3의 배수인지 작성하시오

# number = int(input("정수>"))

# if (number%2==0)  :
#     if number%3==0:
#         print('2와 3으로 나누어집니다')
#     else:
#         print("2로 나누어집니다")
# elif number %3==0:
#     print("3으로 나누어집니다")
# else:
#     print("어느 것으로도 나누어 지지 않습니다")

# set
# - {}을 이용하여 set을 선언
# 

#for i in reversed(range(6)):
#    print(i)

# for count in range(5,-1,-1):
#    print(count)

# 1부터 10까지 합을 구하시오 (range 함수를 이용하시오)

# sum=0
# for i in range(11):
#     sum= sum+i
#     print(sum)


# for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
#         if j <= i:                # 세로 방향 변수 i만큼
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()  

# for i in range(5):
#     for j in r

# for i in range(1,5):
#     print("*")
#     for j in range(1,4,-1):
#         print(" ")
#     for j in range(1,5):
#         print("*")
#     print()

# 계단형
# n = int(input('n:'))
# for i in range(n):
#     print(' '*i,end=' ')
#     print('*'*n)

# # 삼각형
# n = int(input('n:'))
# for i in range(1,n+1):
#         print('*'*i)

# # 역삼각형
# n = int(input('n:'))
# for i in range(1,n+1):
#         print(' '*(n-i),end=' ')
#         print("*"*i)


# n = int(input('n'))
# for i in range(n):
#        print("*"*(n-i))

# n= int(input('n:'))
# for i in range(n):
#        print(' '*i, end=" ")
#        print("*"*(n-i))

# n = int(input("n:"))
# for i in range(1,n+1):
#        print(' '*(n-i), end=" ")
#        print("*"*(2*i-1))

# (1) x=[3,6,9,20,-7,5]의 값의 모든 요소에 10을 곱한뒤 출력하세요
# x=[3,6,9,20,-7,5]
# for i in range(7):
#      print(x[i]*10)

# #심화
# for i in range(0,len(x)):
#      x[i]=x[i]*10
# print(x)
# 심화:출력과 리스트 x의 값에도 모두 10을 곱하세요
#(2) y={"math":70,"science":80,"english":20}의 값의 모든 요소에 10을 더한뒤 출력하세요
# y={"math":70,"science":80,"english":20}
# print(y["key"])

# y={"math":70,"science":80,"english":20}

# for key in y:
#      val = y[key]
#      y[key] = y[key]+10
#      print('%s : %d' %(key,val+10))

# import random

# true_value = random.randint(1,100)
# input_value =99999 #임의의 값 할당
# while True:
#     print("숫자를 맞쳐보세요(1~100)")
#     number = int(input("숫자를 맞쳐보세요(1~100)"))
#     if true_value == number:
#         print(f"정답입니다 입력하신 숫자는{true_value}입니다")
#         break
#     elif number>true_value :
#         print("숫자가 너무 큽니다")
#     elif number<true_value:
#         print("숫자가 너무 작습니다")

# while true_value != input_value:
#     input_value = int(input())

#     if input_value>true_value: #사용자의 입력값이 true_value 클때
#         print("숫자가 너무 큽니다")
#     else:
#         print("숫자가 너무 작습니다") #사용자의 입력값이 true_value보다 작을 때
#     print(f'정답입니다. 입력한 숫자는 {true_value}입니다')

# word = ["shool","game","piano","science","hotel","mountain"] 중 글자수가 6
# 글자 이상인 문자를 모아 새로운 리스트를 생성 하세요
# word = ["shool","game","piano","science","hotel","mountain"]

# list1=[]
# for i in word:
#     if len(i)>=6:
#      list1 = list1.append(word[i])
# print(list1)

# a =list()
# for i in range(len(word)):
#         if len(word[i])>=6:
#            a.append(word[i])
# print(a)


# list =[]
# for i in range(len(word)):
#     if len(word[i])>=6:
#         list.append(word[i])
# print(list)

# 1~100 까지 숫자중
# 3과 5의 공배수일경우 "3과5의 공배수"
# 나머지 숫자중 3의 배수일 경우 "3의 배수"
# 나머지 숫자중 5의 배수일 경우 "5의 배수"
# 모두 해당하지 않을 경우 그냥 숫자를 출력하세요
# b=int(input("정수>"))
# if b<=0:
#     print("음수는 정의하지 않음")
# else:
#     for a in range(1,101):
#         if a%3==0 and a%5==0:
#             print('3과5의 공배수')
#         elif a%3==0:
#             print("3의배수")
#         elif a%5==0:
#             print("5의배수")
#         elif 1<=a<=100:
#             print(a)
#     # 심화 1-입력한 숫자까지의 숫자중

# 사용자로부터 숫자를 계속 입력받다가
# s or S를 입력하면 합계출력



# while True:
#      number = input("값을 입력해주세요>")
#      list1 = []
#      if number=="s" or number=="S":
#          print(sum(a))
#          break
#      else:
#          a = list1.append(int(number))
#          print(a)

# while (d==1):
#     a = (input())
#     if (a=='s'or a=='S'):
#         d=0
#     else:
#         a=int(a)
#         c+=a
# print(c)

# 사람 별 평균을 구하라

# kor_score=[39,69,20,100,80]
# math_score=[32,59,85,30,90]
# eng_score =[49,70,48,60,100]
# midterm_score =[kor_score,math_score,eng_score]

# for i in range(5):
#    (average)= (kor_score[i]+math_score[i]+eng_score[i])/3

#    print(f"{i}:{average}")

# student =[0,0,0,0,0]
# i=0
# for subject in midterm_score: #kor,math,eng 과목선택
#    for score in subject: #과목 선택후
#       student_score[i] +=score #각 학생마다 개별로 교과 점수를 저장
#       #print(subject.score,'i',i,student_score) #kor ->math->eng
#       i +=1 # 학생 index 구분
#       i=0 # 과목이 바뀔 때 학생 인덱스
# else:
#    a,b,c,d,e = student_score # 학생별 점수를 unpacking
#    student_average -[a/3,b/3,c/3,d/3,e/3]
#    print(student_average)

# import numpy as np
# a=np.random.randint(100)
# b=np.random.shuffle(a)


# def add_all(*args):
#     list1=[]
#     list1=list1.append(args)
#     a=sum(list1)
#     print(a)

# add_all(1,2,3,4)

#0~20까지의 숫자를 배열로 만든 다음에 arr1에는 짝수,
#arr2는 홀수가 들어가 배열을 출력해보자

# arr = np.arange(20)
# arr1=([])
# arr2=([])
# if arr%2==0 :
#     arr1=arr1+arr
# elif arr%3==0:
#     arr2=arr2+arr
import pandas as pd
stock = pd.read_csv("https://raw.githubusercontent.com/Youngpyoryu/Lecture_Note/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC/stock_2020_01.csv",encoding='CP949')