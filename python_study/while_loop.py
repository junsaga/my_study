# while 반복문
"""
while 조건:
    반복할 코드
"""

#조건이 참인 경우에 코드를 계속 반복
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# n=1
# while n <=1000:
#     print(n)
#     n += 1 # n = n+1

# +=연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1은 n =n+1이라는 의미
# -=
# n -=1은 n = n-1
# *=
# /=
# **=
# //=
# %=

    # s1 ="안녕"
    # s1 +="하세요" #s1=s1+"하세요"

#while 반복문을 활용하여
#10부터 1까지 순서대로 출력하세요
# n=10
# while n >0:
#     print(n)
#     n -=1

# money =10000
# price =1000
# balance=0
# n=2
# while n<=10:
#       n-=1
#       price=price*n
#       balance=money-price
#       if balance >=0:
#           print("커피를 주문하셨습니다")
#           print("잔액은 {}원입니다".format(balance))
        
# money =10000
# price =1000
# coffee=5
# while money >= price :
#     #while money =price >0:
#     money -=price
#     print(money)
#     coffee -=1
#     print("커피를 구매했습니다.")
#     print("남은커피{}".format(coffee))
#     if coffee ==0:
#         break

# break
# 반복문을 바로 중지한다

# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력

# n=1
# while n<=10:
#     if n%2==1:
#         print(n)
#     n+=1

#continue
#반복문의 제일 처음으로 돌아감
# b=0
# while b<=10:
     
#      if b%2 == 0:
#          continue
#      b+=1
#      print(b)


#무한 반복문
#무한 루프
#조건식에 True를 입력해 항상 참이 되도록 한다
# while True:
#     user_input = input("종료하려면 1을 입력해주세요>")
#     if user_input =="1":
#         break
    

#무한반복문으로 계산기 만들기
#+,-,*,/ 계산
# 2개의 수를 계산

while True:
     print("""
     계산기
     =============
     1.더하기(+)
     2.빼기(-)
     3.곱하기(*)
     4.나누기(/)
     q.종료
     =============
     """)
     operator= int(input("원하는 계산을 고르시오>"))
     a = int(input("숫자를 입력하세오"))
     b = int(input("숫자를 입력하시오"))

     if operator ==1:
         print(a+b)
     elif operator ==2:
         print(a-b)
     elif operator ==3:
         print(a*b)
     elif operator ==4:
         print(a/b)
     elif operator =="q":
         break
     

     # 사용자가 가지고 있는 돈을 입력받는다
     # 몇개의 커피를 구매할 수 있는지와
     # 잔돈을 출력한다
     # 몇개의 음료수를 구매할 수 있는지와
     # 잔돈을