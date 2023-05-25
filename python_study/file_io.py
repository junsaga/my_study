# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
#파이썬 내장 함수
#파일을 열고, 파일 객체를 리턴한다
#open(파일 이름,파일 열기 모드) 
# f = open("C:\Users\405\python_study\새파일.txt","w")
# f.close()
# 파일의 경로
# 절대 경로 : c:/d:/처럼 최상단 경로부터 나타낸 경로
# 상대 경로 : 현재 작업 위치부터 나타낸 경로


# 파일 열기 모드
# r : 읽기 모드,파일을 읽기만 할 때 사용
# w : 쓰기 모드,파일에 내용을 쓸 때 사용
# a : 추가 모드,파일의 마지막에 새로운 내용을 추가할때 사용

# f = open("python_study/새파일.txt",'w')
# for i in range(1,11):
#     print(i,"번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# w 모드는 덮어쓰기 된다


# f=open("python_study/새파일.txt",'a',encoding="utf-8")
# for i in range(11,21): #11~20
#     print(i,"번쨰 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# f=open("python_study/새파일1.txt",'a',encoding="utf-8")
# for i in range(11,21):
#     print(i,"번쨰 줄")
#     f.write(str(i)+"번쨰 줄\n")
# f.close()

# f=open("python_study/새파일.txt",'a',encoding="utf-8")
# for i in range(11,21):
#     print(i,"번쨰 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close

# readline() 함수
# 첫번째 줄부터 1줄 읽어온다
# while True:
#     line =f.readline()
#     if line =="":
#         break
#     print(line)
# f.close()
# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 반환

#readline() 함수
# 첫 번쨰 줄부터 1줄 읽어온다
# while True:
#   line =f.readline()
#   if line =="":
#       break
#   print(line)
#f.close()
# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 반환

#realine() 함수
# 첫 번쨰 줄부터 1줄 읽어온다
# while True:
#   line =f.readline()
#   if line =="":
#       break
#       print(line)
#   f.close()
#   readlines() 함수
#   파일의 모든 줄을 읽어서 리스트로 변환

# f=open("python_study/새파일.txt",'r',encoding="utf-8")
# lines =f.readlines()
# for line in lines:
#     print(lines)
# f.close()

# f=open("python_study/새파일.txt",'r',encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#       print(lines)
# f.close()

#read() 함수
#파일 내용 전체를 문자열로 리턴한다

# f=open("python_study/새파일.txt",'r',encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

# read() 함수
# 파일 내용 전체를 문자열로 리턴한다
# f=open("python_study/새파일.txt",'r',encoding="utf-8")
# data =f.read()
# print(data)
# f.close()

# f=open("python_study/새파일.txt",'r',encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

# with문
# open - close를 자동으로 해준다
# with open("python_study/새파일.txt",'a',encoding="utf-8") as f:
#     f.write("end of file")
#     f.write("2")
#     f.write("3")
#     f.write("4")
# with open("python_study/새파일.txt",'a',encoding="utf-8") as f:
#     f.write("end of file")
#     f.write("2")
#     f.write("3")
#     f.write("4")

# with open("Python_study/새파일.txt",'a',encoding="utf-8") as f:
#     f.write("end of file")
#     f.write("2")
#     f.write("3")
#     f.write("4")

# with open("Python_study/새파일.txt",'a',encoding="utf-8") as f:
#   f.write("end of file")
#   f.write("2")
#   f.write("3")
#   f.write("4")

# # csv(comma separated values)
# # ,로 구분되는 값들을 모아놓은 파일
# # 이름   입실시간,퇴실시간
# # 권오천, 09:20, 18:10
# # 김예진, 09:21, 18:11

# with open("python_study/data.csv","w", encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")

# with open("python_study/data.csv","w", encoding="utf-8") as f:
#   f.write("날짜,날씨,기온\n")
#   f.write("20230423,맑음,10\n")
#   f.write("20230425,비,9\n")



# with open("python_study/data.csv","w", encoding="utf-8") as f"
#     f.write("날짜,날씨,기온\n")
#     f.write("20230423,맑음,10\n")
#     f.write("20230425,비,9\n")
# with open("python_study/data.csv","r", encoding="utf-8") as f:
#     data = f.readlines
#     print(data)

# with open("python_study/data.csv","r", encoding="utf-8") as f:
#   data = f.readlines
#   print(data)

# 계산 결과 저장 함수
# 정수 2개를 입력받고
# 두 수를 더한 결과를 
# add_result.txt 파일에
# 저장하는 함수를 정의하세요
# 함수이름:add_write

def add_write(a,b):
     result = a+b
     with open("python_study/add_result.txt",'w',encoding="utf-8") as f:
         f.write(str(result))



# add_write(1,2)

# def add_write(a,b):
#       result =a+b
#       with open("python_study/add_result.txt","w",encoding="utf-8") as f:
#           f.write(str(result))

# 텍스트 파일에 적힌 정수 2개를
# 읽어와서 더하는 함수를 정의하세요
# 텍스트 파일 이름: add_number.txt
# 경로: python_study/add_number.txt
# 정수 2개를 더한 결과를 print 하세요.
# 함수 이름: read_add_print


# def add_write():
#      with open("python_study/add_number.txt",'r',encoding="utf-8") as f:
#         data = f.read()
#         a=int(data[0])
#         b=int(data[2])
#         print(a+b)
   
# add_write()


# def add_write():
#     with open("Python_study/add_number.txt","r",encoding="utf-8") as f:
#         data =f.read()
#         a=int(data[0])
#         b=int(data[2])
#         print(a+b)

# def add_write():
#     with open("Python_study/add_number.txt","r",encoding="utf-8") as f:
#       data =f.read()
#       a=int(data[0])
#       b=int(data[2])
#       print(a+b)

# def add_write():
#     with open("Python_study/add_number.txt","r",encoding="utf-8") as f:
#       data = f.read()
#       a=int(data[0])
#       b=int(data[2])
#       print(a+b)

# 계산기 만들기
# 기능: 두 정수의 사칙연산(+,-,*,/)
# add(), sub(), mul() , div() 함수 정의
# input() 함수를 상의하여
# 정수 2개, 사칙연산 선택을 입력받은 후
# 계산 결과를 print한다
# 계산신과 결과를
# calculator_request.txt파일에 기록한다
# 사용자가 'q'를 누르면 종료한다
# while True:
        
#             a = int(input("정수1>"))
#             b = int(input("정수2>"))
#             print("1.덧셈,2.뺄셈,3.곱셉,4.나눗셈")
#             n = int(input("번호>"))

#             def add(a,b):
#                 return ((a+b))
#             def sub(a,b):
#                 return ((a-b))
#             def mul(a,b):
#                 return ((a*b))
#             def div(a,b):
#                 return ((a/b))
            
#             if n==1:
#                 n1=add(a,b)
#                 with open("python_study/calculator_result.txt",'a',encoding="utf-8") as f:
#                     f.write(str(n1))
#             elif n==2:
#                 n2=sub(a,b)
#                 with open("python_study/calculator_result.txt",'a',encoding="utf-8") as f:
#                     f.write(str(n2))
#             elif n==3:
#                 n3=mul(a,b)
#                 with open("python_study/calculator_result.txt",'a',encoding="utf-8") as f:
#                     f.write(str(n3))
#             elif n==4:
#                 n4=div(a,b)
#                 with open("python_study/calculator_result.txt",'a',encoding="utf-8") as f:
#                     f.write(str(n4))
#             elif n=="q":
#              break

# 문자열 포매팅(formatting)
# result =str(a)+"/"+str(b)+" ="+str(a/b)
# result = "%d /%d =%d" % 3,2,5
# print(result)
