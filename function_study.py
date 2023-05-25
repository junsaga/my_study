#function 함수
#입력 ->처리 ->출력
# input(입력)을 받아서
# 특정 작업을 수행하고
# ouput(출력)을 반환한다

# 내장 함수(built_in)
# 파이썬이 기본적으로 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

# abs()
# absoluet의 약자
# 숫자형 데이터의 절댓값을 반환한다
# print(abs(100))
# print(abs(-100))
# print(abs(3.14))
# print(abs(-3.14))



# sum(리스트)
# 리스트 안의 숫자를
# # 더한 값으로 반환한다
# print(sum([1,2,3,4,5]))

# #max(리스트)
# # 리스트 안에서 최댓값을
# # 찾아 반환한다
# print(max([1,2,3,4,5]))

# #min(리스트)
# # 리스트에서 최솟값을
# # 찾아 반환하다
# print(min([1,2,3,4,5]))

# print(min([1,2,3,4,5]))
# li_1 =[1,2,3]
# min(li_1)
# li_1.append(4)

# chr(정수)
# 정수 1개를 입력받고 
# # 해당 정수에 해당하는
# # 유니코드 문자를 반환한다
# print(chr(65))  #A
# # ord(문자)
# # 문자 1개를 입력받고 해당한느
# # 정수를 반환하다

# print(ord('A')) #65

# # round(값)
# # rounde(값,소수 자릿수)
# # 반올림 함수
# print(round(1.234))
# print(round(1.234,2)) #1.23
# print(round(1.369,1)) #1.4

# # 함수 정의(define)
# # 함수 이름
# # 함수 입력값 parameter
# # 함수 결과 return value
# """
# def 함수이름(함수 입력값):
#     함수기능코드
#     return 함수 결과값
# """

# # def 함수를 정의하는 명령어
# # 함수이름도 변수 이름처럼
# # 규칙을 지켜서 지어야 한다
# # 영어,숫자,_만 사용
# # 띄어쓰기 하면 안됨
# # 키워드 사용하면 안됨
# # 기존에 이미 정의된 함수이름도
# # 피하는 것이 좋음

# def print_names():
#    print("손흥민")
#    print("황의찬")
#    print("김민재")
#    print("이강인")

# return 값이 없으므로 변수의 담을 수 없다
# print_names()

# def get_name():
#     return "전세계"
# #return 값이 있으면 변수의 담을 수 있다

# def print_my_name():
#     a=print(10)
#     b=range(10)

# def print_my_names():
#     a =print_names() #리턴이 없음
#     b =get_name() #리턴이 있음
#     print(a)
#     print(b)

# parameter
# 함수에 입력하는 값
# 매개변수, argument 혼용
def add(a,b):
    return a+b


# def print_add(a,b):
#    print(a+b)

# result = add(1,2)
# print(result)

# result = print_add(1,2)
# print(result)

# # print_add("안녕")
# print_add(1,2)
# print_add("안녕","하세요")
# #숫자와 문자는 +기가 안된다
# #print_add("안녕"+1) #오류
# print_add("하세요","안녕")
# print_add( b="하세요",a="안녕")
# #매개변수를 지정해버리면 


# def swap_number(a,b):
#     temp =a
#     a = b
#     b = temp
#     print(a,b)
#     return a,b
# swap_number(1,2)
# #결과:2,1

# a =1
# b =2
# print("함수 호출 전",a,b)
# a,b =swap_number(a,b)
# print("함수 호출 후",a,b)
#함수 내부에서 쓰는 매개변수와 함수외부에서 쓰는 매개변수는 다르다
#그러므로 함수 외부에서 함수 내부로 매개변수를 쓸때 global을 사용해서 매개변수를 쓴다

# 다음 함수를 정의 하세요
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

# def mul(a,b):
#     return (a*b)

# print(mul(1,2))

# #기본 값 매개변수
# # default value parameter
# # 함수 호출 시 n2에 입력된
# # 값이 없으면 기본 값 사용
# def mul(n1,n2=1):
#     return n1*n2

# mul(1,2)
# mul(1)
# # n2에는 기본값 1

# def test_func1(x,test=5):
#     test =test
#     print(x,test)

#     test_func1(1)
#     test_func1(2)

# # list는 지역변수에도 불구하고 전역변수로 공유
# # 기본값으로 list는 사용하면 안된다

# def test_func2(x,test=None):
#     if test == None:
#         test =[]
#     test.append(x)
#     print(x, test)

# # def sub(n1, n2=0, n3):    # 기본값이 설정된 매개변수는 무조건 뒤로 보내야 한다
# #     print(n1 - n2 - n3)

# def sub(n1,n3,n2=0): 
#   print(n1 - n2 - n3)

# 1~10까지 더한다
# *를 사용한 매개변수
# 입력값이 몇개가 될지
# 모를 때 (안 정해졌을 때)
# def add_many(*args):
#     #튜플처럼 사용
#     #인덱싱,슬라이딩
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(add_many(1,2,3,4,5,6,7,8,9,10))

# def calc_many(n1,*args):  #순서를 바꿔서도 사용가능하다
#     result = n1
#     for i in args:
#         result +=i
#     return n1

# def add_many(*args):
#     i = sum(args)
#     return i

# 키워드 매개변수
# **kwargs
# keyword arguments
# 딕셔너리로 사용

#뒤에 오는 값들이 유동적일때 사용
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1,b=2)
# print_kwargs(name="이름",age=10)


#함수의 반환
#return 반환값
#return을 만나면 반환값을 반환함과 동시
#에 함수가 종료

def test_func():
    print(1)
    print(2)
    return None
    print(3)
    print(4)
    print(5)

test_func()

#함수의 반환값은 무조건 1개이다
def test_func6(a,b):
    return a+b,a*b #묶어서 리턴해야한다
    return a*b
result =print(test_func6(8,9))
res_add,res_mul =test_func6(1,2)
#res_add, res_mul =(a+b,a*b)
print(result)
print(res_add,res_mul)

def test_func6(a,b):
    return a+b,a*b #묶어서 리턴해야 한다
result =print(test_func6(8,9))
res_add,res_mul =test_func6(1,2)
print(result)
print(res_add,res_mul)

