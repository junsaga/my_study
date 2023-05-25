# 객체지향(oop,object oriented programming)
# 객체와 객체 사이의 상호작용으로 프로그램을
# 구성한다 프로그래밍 패러다임

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출
# 캡슐화 : 데이터의 구조와 연산을 결합한다
# 상속 : 상위 개념의 특징이 하위 개념에 전달
# 다형성 : 유사 객체의 사용성을 그대로 유지

# 객체는 추상화와 캡슐화의 결과
# 객체는 데이터 필드와 메소드를 가진다
# 클래스는 객체를 정의하는 것(객체의 설계도)
# 데이터 필드(멤버 변수,속성)
# 객체가 가지고 있는 변수
# 메소드
# 객체가 가지고 있는 함수

"""
class 클래스이름:
    클래스 멤버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙 지켜야 함
# 클래스 이름 컨벤션(관용)
# 첫 글자 대문자
# 언더바(_) 안쓰기
# # 단어 구불될 떄 대문자

# class Car:
#     def move(self):
#         print("move")


# class SportsCar:
#     pass

# # 인스턴스
# # 클래스를 통해 생성된 객체
# my_car = Car()
# my_car.move()
# # . --------> 객체 맴버 접근 연산자
# li = [1,2,3,4,5]
# li.append(6)

# # 파이썬에서는 모든게 객체다

# # 내장함수 type()
# # 데이터의 자료형을 반환한다
# # list라는건 list라는 클래스가 정의되어있다
# print(type(li))
# n=10
# print(type(n))
# print(type("Hello"))

# #str(문자열) 메소드
# # upper()
# # 모두 대문자로 변경
# s ="Hello"
# print(s.upper())
# print(s.lower())
# # strip()

# #lstrip() rstrip()
# # 왼쪽, 오른쪽 끝의 특정 문자 제거
# # 문자열 양쪽 끝의 특정 문자를 제거
# s1 ="    Hello   "
# print(s1.strip())
# print(s1.rstrip())
# print(s1.lstrip())

# #split()
# # 구분자로 분할하여 리스트로 반환
# s2 ="Hello,World,Python"
# print(s2.split(','))
# # replace()
# # 문자열의 특정부분을 대체
# print(s2.replace(',',' '))
# print(s2)
# s2 =s2.replace(',',' ')
# print(s2)

# # "Hello" ---> "hello"
# # string은 수정이 불가능하다
# # immutable이라 불가능
# # replace 함수를 사용하여 
# s3 ="Hello"
# s3[0]  ="h"
# s3.lower()
# s4 = s3.replace("H","h") 
# print(s3)

# self 매개변수
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는
# 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된
# 멤버에 접근할 때 사용

# class Person:
#     def say(self):
#         self.name = "사람1"
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self,food):
#         self.sleep()
#         print(f"{self.name}이 {food}를 먹었습니다")

#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다")

# person1 = Person()

# person1.say()
# person1.eat("피자")

# initializer 초기자
# initialize 초기화
# class Person:
#     def __init__(self,name,age,gender,phone):
#         self.name = name
#         self.age =age
#         self.gender =gender
#         self.phone = phone
#         print("initialize")

#     def say_name(self):
#         print(self.name)
    
#     def introduce(self):
#         print(f"저의 이름은 {self.name}이고 나이는 {self.age} 성별은 {self.gender} 전화번호는{self.phone}입니다")
        
# print("before")
# person2 = Person("홍길동","20", "남자","010-1234-5678")
# print("after")
# person2.say_name()
# person2.introduce()
# #클래스 매개변수에 초기값을 입력받을때


# Person 클래스에 introduce 메소드를 추가
# 이름,나이,성별을 print하는 메소드

# 상속 inheritance

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

class Student:
    def __init__(self,name,age,school,grade):
        # 이름,나이,학교,학년을 멤버 변수로
        # 저장하는 메소드를 정의하세요, 
      self.name=name
      self.age=age
      self.school=school
      self.grade=grade
    
    def introduce(self):
       print(f"{self.name},{self.age},{self.school},{self.grade}")


st1_int = Student("철수","19","냉장고","3")
st2_int = Student("영희","19","렛잇고","3")
st3_int = Student("유리","19","아이고","3")
st4_int = Student("서현","19","유기고","3")
stu_list =[st1_int,st2_int,st3_int,st4_int]
for stu in stu_list:
   stu.introduce()