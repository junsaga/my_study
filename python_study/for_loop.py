# for문
"""
for 변수 in iterable값:
    반복할 코드
"""

# li_1 =["one","two","three"]
# for i in li_1:
#     print(i)

# # 첫번째 요소부터 마지막 요소까지
# # 변수에 대입하면서 반복
# # s1 ="hello"
# # for i in s1:
# #     print(i)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     print(i)


# numbers.reverse()
# for number in range(100):
#     print(number)

# range()
# 숫자 range 객체를 만들어 주는 함수
# range(끝 정수)
# 0~끝 정수-1
# range(시작, 끝)
# 시작~끝 -1
# range(시작,끝,스텝)
# 시작~끝 -1 까지인데 스텝만큼 차이나게

# for i in range(11) :
#     print(i)

# for i in range(0,21,2):
#     print(i)

# from math import sin,cos,tan,floor,ceil
# sin(1)
# cos(1)
# tan(1)
# floor(2.5)
# ceil(2.5)

# #for문을 사용하여 2부터 30까지 출력해보세요
# for i in range(2,31):
#     print(i)


# print()
# #for문을 사용하여 2부터 30까지 숫자 중
# #짝수만 출력해보세요
# for i in range(2,31,2):
#     print(i)

# for i in range(2,31):
#     if i%2==1: # 홀수
#        # continue
#         pass # 아무것도 안하고 그냥 넘어갈때
#     else: #짝수
#         print(i)
#     print("반복")

# if 1 ==1:
#     pass
#     print("완료")


# for i in range(5):
#     pass
# print("완료")
# print()

# for i in range(2,31):
#     if i %2==0: # 짝수
#         print(i)

# # #for문을 사용하여 10부터 1까지 출력해보세요
# # for i in reversed(range(1,11)):
# #     print(i)

# for i in range(1,11)[::-1]:
#     print(i)
# #   [시작인덱스:끝인덱스:뱡향]



# print()

# import math as m
# m.sin(1)
# m.cos(1)
# m.tan(1)
# m.floor(2.5)
# m.ceil(2.5)


# import random
# print("# random 모듈")

# #random(): 0.0<=x<1.0 사이의 float를 리턴합니다
# print("- random():",random.random())

# #uniform(min,max): 지정한 범위 사이의 float를 리턴합니다
# print("-uniform",random.uniform(10,20))

# #randrange():지정한 범위의 int를 리턴합니다
# #-randrange(max): 0부터 max 사이의 값을 리턴합니다
# #-randrange(min): min부터 max 사이의 값을 리턴합니다
# print("-randrange(10):",random.randrange(10))

# #choice(list):리스트 내부에 있는 요소를 랜덤하게 선택합니다
# print("-choice[1,2,3,4,5]:",random.choice([1,2,3,4,5]))

# #shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다
# print("-shuffle([1,2,3,4,5]):",random.shuffle[1,2,3,4,5])

# #sample(list,k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다
# print("-sample([1,2,3,4,5],k=2)",random.sample([1,2,3,4,5],k=2))


# #모듈을 읽어 들입니다
# import sys

# #명령 매개변수를 출력합니다
# print(sys.argv)
# print("---")

# #컴퓨터 환경과 관련된 정보를 출력합니다
# print("getwindowsversion:()",sys.getwindowsversion)
# print("---")
# print("copyright:",sys.copyright)
# print("---")
# print("version",sys.version)

# #프로그램을 강제로 종료합니다
# sys.exit()

# money =10000
# price =1000
# coffee =5
# for i in range(1,6):
#      price =price*i
#      print("커피를 구매했습니다")
#      money=money-price
#      coffee=coffee-1

#      print("남은 커피 :{}".format(coffee))
#      print("잔돈 :{}".format(money))

# prices=[500,700,930]
# for price in price:
#     print(money // price)
#     print(money % price)


# for i in range(1,coffee+1): #1~5
#     print("남은 커피:",coffee -i) #4~5

# for i in range(coffee):
#     coffee -=i
#     print("남은 커피 :",coffee)

# # 모듈을 읽어 드립니다 
# from urllib import reques

# # urlopen() 함수로 구글의 메인페이지를 읽습니다
#     target =request.uropen("https://goggle")

# scores =[]
# for i in range(5):
#     score =int(input("시험점수:"))
#     scores.append(score)
#     print(scores)

# 이중 for 문
for i in range(2,10): # 1~9
    print(i,"단")
    for j in range(1,10):    
        print(i*j)
    print("------------------")