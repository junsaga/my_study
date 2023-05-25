# max_limit_calculator.py 파일에 작성하세요
# my_calculator 모듈의 MyCalculator 클래스를
# 상속받아서 MaxLimitCalculator 클래스를 정의하세요
# add,sub,mul,div 메소드를 사용하여
# 더하기,뺴기,곱하기, 나누기를 할 수 있다
# 0으로 나눴을 때 에러가 발생하지 않도록 처리한다
# 입력되는 정수가 1개라도 100보다 크면 계산하지 않고
# 100 이하의 값을 입력하도록 안내 메세지를 출력한다


from MyCalculator import MyCalculator1

class MaxLimitCalculator(MyCalculator1):
    def add(self,n1,n2):
        if n1 >100:
            print("100보다 작은 수를 입력하세요")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요")
        else:
            result = n1+n2
            if result >100:
                print("계산결과가 100보다 작아야합니다")
            else:
                print(f"{n1}+{n2} ={n1+n2}")

    def sub(self,n1,n2):
        if n1 >100:
            print("100")
        elif n2 >100:
            print("100")
        else:
            result =n1 -n2
            if result > 100:
                print("100")
            else:print(f"{n1}-{n2}={n1-n2}")
    def mul(self,n1,n2):
        if n1 >100:
            print("100")
        elif n2 >100:
            print("100")
        else:
            result = n1 *n2
            if result >100:
                print("100")
            else:
                print(f"{n1}*{n2}={n1*n2}")
    def div(self,n1,n2):
         if n1 >100:
            print("100")
         elif n2 >100:
            print("100")
        #  elif n2==0:
        #      print("0")
         else:
            try:
                result = n1/n2
            except ZeroDivisionError:
                print("0으로 나누지 마세요.")
            if result >100:
                print("100")
            else:
                print(f"{n1}/{n2}={n1/n2}")

my_max_limit_calculator = MaxLimitCalculator()
my_max_limit_calculator.add(100,200)
#   try:
#     while True:
#         n1=int(input("정수1>"))
#         n2=int(input("정수2>"))
#         calculator1 = MyCalculator1(n1,n2)
#         operator = input("입력값>")
#         if operator =="1":
#             if n1>100 or n2>100:
#                print("100이상의 값을 입력할 수 없습니다")
#             else:calculator1.add(n1,n2)
#         elif operator =="2":
#               if n1>100 or n2>100:
#                print("100이상의 값을 입력할 수 없습니다")
#             calculator1.sub(n1,n2)
#         elif operator =="3":
#               if n1>100 or n2>100:
#                print("100이상의 값을 입력할 수 없습니다")
#             calculator1.mul(n1,n2)
#         elif operator =="4":
#               if n1>100 or n2>100:
#                print("100이상의 값을 입력할 수 없습니다")
#             calculator1.div(n1,n2)
#         elif operator =="q":
#             break
#   except ZeroDivisionError as e:
#      print(e,"0으로 나눌 수 없습니다")
#   except IndexError as e:
#      print(e,"인덱싱할 수 없습니다.")
      
# class Animal:
#     def __init__(self, name):
#         self.name =name
#         print(f"{self.name}이(가) 생성되었습니다")
    
#     def say(self):
#         print("")

# class Dog(Animal):
#     # 메소드 재정의 
#     # method overriding 덮어쓰기
#     def say(self):    
#         print("멍멍")

# my_dog =Dog("백구")
# my_dog.say()

# class Cat(Animal):
#     def say(self):
#         print("야옹야옹")

# my_cat =Cat("나비")
# my_cat.say()
