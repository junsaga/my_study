# 2~9사이의 숫자를 입력받아
# 해당하는 단의 구구단을 출력하세요
# 2~9 사이의 숫자가 아닌 값이
# 입력된 경우, 잘못 입력되었다고
# 출력하고 다시 입력받으세요/

# for i in range(2,10):
#     print("{}단입니다".format(i))
#     for j in range(1,10):
#         print("{}*{}={}",i,j,i*j)

# while True:
#         number1 = int(input("숫자>"))
#         number2 = int(input("숫자>"))
        
#         if 2<= number1 <=9  and 2<=number2<=9 :
#             for i in str(number1):
#                  print("{}단입니다".format(i))
#                  for j in range(1,number2+1):
#                       print(int(i)*j)
#         else :
#             print("범위에 값이 아닙니다")

# # 2~9 사이의 값일 때 True
# if n>=2 and n<=9:
#      pass
# if 2<= n <=9:
#      pass
#      #구구단을 출력하는 코드
# # 2<= n <=9 -----> 2~9사이라면 True
# while not 2<= n <=9:
#      print("2~9 사이의 숫자를 입력해주세요.")
#      n = int(input("몇 단?"))
# for i in range(1,10):
#       print(n,"*", i,"=")



#정수를 입력받고
#그 정수보다 작은 수 중
#가장 큰 제곱수를
#출력하세요
# while True:
#     n= int(input("정수"))
# # i=1
# # while True:
# #     # i**i
# #     if i **2 > n:
# #         break
# #     answer =i **2
# #     i +=1
# # print(answer)
#     i=1
#     while i>0:
#         i+=1
#         if ((i-1)**2)< n <(i**2):
#             print((i-1)**2)

#[1,2,3,4,5]
#[10,20,30,40,50]
#[532,5941,54682,58,5]
#3개의 리스트에서 같은 인덱스의
#값끼리 더하여 출력하세요
li_1=[1,2,3,4,5]
li_2=[10,20,30,40,50]
li_3=[532,5941,54682,58,5]

for x,y,z in zip(li_1, li_2, li_3):
    print(x+y+z)
i =0

while i <5:
    print(li_1[i]+li_2[i]+li_3[i])
    i +=1

# zip()
# 길이가 같은 list를 묶어서 for문 등으로 
# 사용가능한 iterable을 반환한다


#정수를 입력받고 1부터 입력받은
#정수까지 모두 출력하세요
#단, 숫자에 3,6,9가 들어있는
#경우 숫자 대신 짝이라고
#출력하세요

number=(input("숫자>"))
for i in range(int(int(number)+1)):
      for s in range(len(str(i))):
        str_num=str(i)[s]
        if str_num in "369":
            print("짝")
        else:
            print(i)

# for i in range(number):
#     output=filter(lambda x:x%3==0,number)

# with open("basic.txt","w") as file:
#     #파일에 텍스트를 씁니다
#     file.write("Hello Python Programming")

# for 한 줄을 나타내는 문자열 in 파일 객체:
# 처리

# with open("info.txt","r") as file:
#     for line in file:
#         #변수를 선언합니다
#         (name,weight,height) = line.strip().split(",")
#데이터가 문제없는지 확인합니다 문제가 있으면 지나감

# 정수를 입력받고 그 정수의 약수를
# 모두 출력하세요
# 약수 : 나누었을 때 나머지가 0으로 나누어 떨어지게 하는 수

# n = int(input("정수>"))

# for i in range(1,n+1):
#         if n%i==0:
#             print(i)