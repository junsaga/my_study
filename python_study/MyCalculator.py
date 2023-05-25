#MyCalculator 클래스를 만들어 보세요
#add, sub, mul, div 메소드
class MyCalculator1:
           
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def add(self,a,b):
        print(f"{a}+{b}={a+b}")
    def sub(self,a,b):
        print(f"{a}-{b}={a-b}")
    def mul(self,a,b):
        print(f"{a}*{b}={a*b}")
    def div(self,a,b):
        print(f"{a}/{b}={a/b}")
        

if __name__=="__main__":
    while True:
       
        n1 = int(input("정수1>"))
        n2 = int(input("정수2>"))
        my_calculator = MyCalculator1(n1,n2)
        print("계산기 1.+|2.-|3.*|4./")
        operator = int(input("번호>"))
        if operator ==1:
            my_calculator.add(n1,n2)
        elif operator ==2:
            my_calculator.sub(n1,n2)
        elif operator ==3:
            my_calculator.mul(n1,n2)
        elif operator ==4:
            my_calculator.div(n1,n2)
    
# class Student:
#     def __init__(self,name,age,school,grade):
#         # 이름,나이,학교,학년을 멤버 변수로
#         # 저장하는 메소드를 정의하세요, 
#       self.name=name
#       self.age=age
#       self.school=school
#       self.grade=grade
    
#     def introduce(self):
#        print(f"{self.name},{self.age},{self.school},{self.grade}")


# st1_int = Student("철수","19","냉장고","3")
# st2_int = Student("영희","19","렛잇고","3")
# st3_int = Student("유리","19","아이고","3")
# st4_int = Student("서현","19","유기고","3")
# stu_list =[st1_int,st2_int,st3_int,st4_int]
# for stu in stu_list:
#    stu.introduce()