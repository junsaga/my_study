# 다음 함수를 정의하세요
# 정수 n을 입력받고, n보다 
# 작은 수 중 3의 배수와
# 5의 배수를 모두 더한 합을
# 반환하는 함수
# 함수 이름 : sum_3_5



# def sum_3_5(n):
#    result =0
#    for i in range(n):
#        if i%3==0 or i%5==0:
#          result +=i
#         return result

# def sum_3_5(n):
#      result =0
#      for i in range(n):
#           if i%3==0 or i%5==0:
#                result +=i
            
#      return result 
# sum_3_5(16)
# def sum_3_5(n):
#          i=1
#          while n>i:
#             if i%3==0 or i%5==0:
#                 i+=1
#                 i+=i
#             else:
#                 i+=1
#             return i

# print(sum_3_5(6))


# 정육면체 주사위 2개가 있다
# 2개의 주사위를 던졌을때
# 나올 수 있는 주사위 눈의 조합을
# 모두 print하는 함수를 정의하세요
# 함수이름 : draw_dice
# 출력예시
# 1,2
# 6,3

# def draw_dice(n1=7,n2=7):
#      for i1 in range(1,n1):
#           for i2 in range(1,n2):
#                print("({},{})".format(i1,i2))

# draw_dice()

# i=1 
# while i<7:
#         j=1
#         while j<7:
#             print(i,j)
#             j +=1
#         i +=1
# print(i,j)

# output=""



#두 수의 차이를 구하는 함수
#함수에 입력된 두 정수의 차이를
#계산하고 반환하는 함수를 정의하세요
#함수 이름: get_diff

# def get_diff(n1,n2):
#     if n1>n2:
#         return n1-n2
#     elif n1<n2:
#         return n2-n1

# print(get_diff(1,2))

# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개 정수를
# 사용하여 만들 수 있는 가장 큰
# 수를 반환하는 함수를 정의하세요
# 함수이름 : get_biggest



# def get_bigges(*args):
#     numbers = args
#     n1=numbers.sort(reverse=True)
#     n2=(''.join(str(n1)))
#     s=int(n2)
#     return print(s)

# get_bigges(1,2,3,4,5)


# def get_bigges(a,b,c,d,e):
#     numbers.sort()
#     numbers =[1,2,3,4,5]
#     result =0
#     for i in range(len(numbers)):
#         result += numbers[i]*(10**i)
#     return result

# get_bigges('1','2','3','4','5')


def print_starts(n1):
      output=""
      for i in range(1,n1):
             for j2 in (range(4,i,-1)):
                     output +=" "        
             for j1 in (range(i)):
                     output +="*"
             output +="\n"
      print(output)


print_starts(5)

# def print_stars2(n):
#     for i in range(1, n+1):
#         print(""*(n-i)+"*"*i)

