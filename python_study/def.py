# # def add(a,b):
# #     result = a+b
# #     return result
# # # 함수 정의하기
# # # return이 없는 함수

# # a=[1,2,3,4,5]
# # # 1번 함수
# # def swap_value(x,y):
# #     temp =x
# #     x =y
# #     y =temp

# # # 2번 함수
# # def swap_offset(offset_x,offset_y):
# #     temp =a[offset_x]
# #     a[offset_x]=a[offset_y]
# #     a[offset_y] =temp

# # # 3번 함수
# # def swap_reference(list,offset_x,offset_y):
# #     temp =list[offset_x]
# #     list[offset_x] = list[offset_y]
# #     list[offset_y] =temp

# # swap_value(a[1],a[2])
# # print(a) # [1,2,3,4,5] swap 발생 안함
# # swap_offset(1,2)
# # print(a)
# # swap_reference(a,1,2)
# # print(a)

# #함수를 만들어보자
# # - 이 함수는 두 개의 숫자를 input으로 받으면 작은 수로 큰수를 나눈 몫과 나머지를 반환하는 함수이다
# # - 반환 값은 튜플로 되어 있으며 몫,나머지 순으로 되어 있다
# # - 단,0으로 나누는 것은 불가능하기 때문에 두수중에 작은 수가 0이라면 화면에 '0은 사용할 수 없습니다'를 출력하고 종료되어야 한다
# # while True:
# #     num1 = int(input('정수1>'))
# #     num2 = int(input('정수2>'))

# #     def  div(num1,num2):
# #         if num1>num2:
# #             print(f"몫:{num1//num2}나머지:{num1%num2}")
# #         elif num1<num2:
# #             print(f"몫:{num2//num1}나머지:{num1%num2}") 
# #         elif num1 ==0 or num2 ==0 :
# #             print("0은 사용할 수 없습니다")
            
            

# # def div(a,b):
# #     if a<b:
# #         big=b
# #         small=a
# #     elif b<=a:
# #         big=a
# #         small=b
# #     else:
# #         print("정수가 아닙니다")
# #     if small ==0:
# #         print('0은 사용할 수 없습니다')
# #     elif abs(big)<0 or abs(small)<0:
# #         print('정수를 입력해주세요')
# #     else:
# #         q = big//small
# #         r = big%small
# #         return (q,r)          

# #     div(0,0)      

# # def test(*args):
# #     print(args)

# #  어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 짜보자 
# #  끊는 단위는 따로 정하지 않으며 2로 설정해 보자
# # hint
# #
# # def func(string, unit=2):
# #     i=0
# #     while i<len(string):
# #         print(string[i:i+unit])
# #         i +=unit
# # func("안녕하세요",2)

# # def test(*args):
# #     print(args)


# # test(1,2,3,4,5,6,7,8,9,10)
# # test([1,2],3)
# # test([1,2])

# # def test(*a):
# #     print(a)

# # test(1,2,3,4,5,6,7,8,9,10)
# # test([1,2],3)
# # test([1,2])

# # def test2(**kwargs):
# #     print(kwargs)

# # test2(a=1,b=2,c=3)
# # def add_all(*args):
# #                 list1=[]
# #                 list1.append(args)
# #                 for i in range(len(list1)):
# #                         sum = sum+list1[i]
# #                         print(sum)


# # add_all(1,2,3,4,5,6,7,8,9,10)

# # def add_all3(*args):
# #         s=0
# #         for i in args:
# #                 for j in i:
# #                         s +=j
# #                 return s
# # add_all3([1,2,3,4,5,6,7,8,9,10])

# # def add_all4(*args):
# #     temp=0
# #     for i in range(len(args)):
# #         if type(args[i]) == list:
# #             for j in args[i]:
# #                 temp +=j
# #             else:
# #                 temp +=args[i]
# #         return temp

# # add_all4([1,2,3,4,5,6,7,8,9,10])

# #팩토리얼을 구하시오

# # def Factorial(n):
# #     if n==0:
# #         Factorial(0)==1
# #     elif n==1:
# #         Factorial(1)==1
# #     elif n>=2:
# #         Factorial(n)*Factorial(n-1)

# # 재귀적으로 하지 않은 것
#     # def fact(n):
#     #     f=1 #곱을 계산할 변수의 초깃값
#     #     for i in range(1,n+1): #1부터 n까지 반복
#     #         f= f*i #곱셉연산
#     #     return f

# # 재귀적으로 하는 것
#     # def fact(n):
#     #     if n<=1:
#     #         return 1
#     #     return n*fact(n-1)

# # people =['펭수','뽀로로','뚝딱이','텔레토비']
# # def func1(list):
# #     for i in range(4):
# #         print(f"대기번호{i}번: {people[i]}")
# # lines = func1(people)
   
# # def func1(line):
# #     new_lines =[]
# #     i=1 #대기번호를 트래킹하는 변수 i
# #     for x in line:
# #         print("대기번호 %번 : %s" %(i,x))
# #         new_lines.append((i,x))
# #         i +=1 #별도로 업데이트를 해줘야 함
# #     return new_lines

# # enumerage(열가하다)
#         # 반복 가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수

# # lst =['a','b','c']
# # for x in enumerate(lst):
# #     print(x)

# # lst1 = 'abcd'
# # for x in enumerate(lst1):
# #     print(x)

# # def func1(line):
# #     new_lines =[]
# #     for idx,val in enumerate(line):
# #         print("대기번호 %d번: %s" %(idx,val))
# #         new_lines.append(idx+1,val)
# #     return new_lines

# # -zip
#     # 반복 가능한 객체들을(2개 이상) 병렬적으로 묶어주는 함수
#     # 각 원소들을 튜플의 형식으로 묶어줌

# # str_list =['one','two','three','four']
# # num_list =[1,2,3,4]

# # for i in zip(num_list,str_list):
# #     print(i)
# # squared =[]
# # for i in items :
# # 	squared.append(i*i)

# # print(squared)

# # [1,4,9,16,25]

# # squared_map =list(map(lambda x: x**2,items))

# # print(squared_map)
# # [1,4,9,16,26]

# # items = [1,24,3,6,7]
# # str_items = list(map(lambda x: str(x),items))

# # print(str_items)

# #구구단 2단을 list comprehension을 이용하여 구현하고 리스트를 화면에 출력해보자
# # list_2 =[]
# # for x in range(1,10):
# #     print(f"{x}*{2}={x*2}")

# lc_1 =[x for x in range(10)]

# #1) 구구단2단
# table =[2*x for x in range(1,10)]
# print(table)

# #2) 코로나 바이러스
# setnece="코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 마스크를 끼고 손씻기를 생할화합시다".

# len_sent =[len(s) for s in setnece.split()]
# print(len_sent)


# # 다음의 문장을 분석해보자
# #"코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 마스크를 끼고 손씻기를 생
# # 할화합시다." 라는 문장을 띄어쓰기별로 분석하려고 한다 띄어쓰기별로 문장을 나눈 후 각 요소의
# # 길이를 리스트에 저장하라
# # Hint 띄어쓰기는 split 함수를 써라

# # 10부터 20까지 

# list3=[]
# for x in range(10,21):
#     if x%2==0:
#         list3.append(x)
#     print(list3)

# lc_2 =[x for x in range(10,21) if x%2==0]
# print(lc_2)

# # 1부터 10의 제곱수 중 50이하인 수만 리스트에 저장하라
# list1=[]
# # for x in range(1,11):
# #     if (x**2) <50:
# #         list1.append(x**2)
# # lc_3 = [x**2 for x in range(1,11) if (x**2)<50]
# # print(lc_3)
# # sentece="코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 마스크를 끼고 손씻기를 생할화합시다"
# # lc_4 =[s for s in sentence.split() if len(s)<5]
# # print(lc_4)

# # list_4=[]

# # for x in range(1,11):
# #     if x%2==1:
# #         list_4.append(x**2)
# #     else:
# #         list_4.append(x**3)
    
# #     [x**2 if x%2==0 else x**3 for x in range(1,11)]

# # for문 + for문

# word1='hello'
# word2='world'

# result = [i+j for i in word1 for j in word2]
# result

# # 40이하의 숫자는 5를 더하고 40초과의 숫자는 41로 바꾸어 리스트
# list1=[]
# for i in range(1,101):
#     if i <=40 :
#         i=i+5
#         list1.append(i)
#     elif i>40:
#         i==41
#         list1.append(i)

# print(list1)


# # 컷트라인이 60점일때, 사람이름과 통과여부를리스트로 담아서 출력하라
# # 이름과 통과여부는 튜플로 묶여있는 자료이다

# student = {
#         "보라돌이":61,
#         "뚜비":35,
#         "나나":78,
#         "뽀":88
#            }

# def func1(line):
#      new_lines =[]
#      for idx,val in enumerate(line):
#          print("대기번호 %d번: %s" %(idx,val))
#          new_lines.append(idx+1,val)
#      return new_lines
# def func1(line):
#     student = {
#         "보라돌이":61,
#         "뚜비":35,
#         "나나":78,
#         "뽀":88
#            }
#   result =[(name,True) if score>60 else (name,False)for name,score in students.items()]
#   result 

a= np