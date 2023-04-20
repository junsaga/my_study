#eng 변수,kor변수,math 변수를 만들고 
#각 변수는 과목의 시험 점수이다
#3 과목 점수의 편균을 내고 평균 점수에 따라 성적을 출력한다
# while(True):
#     name =input("이름을 입력하시오>")
#     eng = int(input("영어점수를 입력하시오>"))
#     mat = int(input("수학점수를 입력하시오>"))
#     kor = int(input("국어점수를 입력하시오>"))

#     total=eng+mat+kor
#     average=total/3

#     if average>90:
#         score="A"
#     elif average>80:
#         score="B"
#     elif average>70:
#         score="C"
#     elif average>60:
#         score="D"
#     else:
#         score="F"

#     list1 = []
#     list2 = []
#     list1 =list()
#     list2 =list()

#     list1.append(name)
#     list2.append(score)
    
    
#     dictionary = {
#         "name":list1,
#         "score":list2
#     }

#     for key in dictionary:
#         for student in dictionary[key]:
#             print(key+":"+student)
    

#     print(dictionary)
#     print(list1)
#     print(list2)

    # A:91~100
    # B:81~90
    # C:71~80
    # D:61~70
    # else:F

    #나이와 가지고 있는 돈을 입력받는다
    #가지고 있는 돈으로 물건을 몇개 살수있는지와 잔돈을 출력한다
    #물건의 가격은 500원이다

    #나이와 가지고 있는 돈을 입력받는다
    #가지고 있는 돈으로 물건별로 각각
    #몇 개 살 수 있는지와 잔돈을 출력한다
    # 물건의 가격은 1번 물건 1000원
    # 2번 물건 50원 3번 물건120원이다

# age=input("나이>")
# money=int(input("돈>"))

# stuff1=1000
# stuff2=50
# stuff3=120

# age =input("나이:")
# money =int(input("돈:"))
# price =[1000,50,120]

# print(money //price[0],money % price[0])
# print(money //price[1],money % price[1])
# print(money //price[2],money % price[2])

# while True:
#             print("#가격:1.커피:1500 2.음류수700:,3.콜라:930")
#             print("#종류:1.커피 2.음류수 3.콜라")
#             stuff=int(input("음류 종류>"))
#             money = int(input("금액>"))
#             if stuff==1 and money>=1500:
#                 stuff =1500
#                 pos_num=money//stuff
#                 balance =money-stuff
#                 print("커피가 주문되었습니다.잔액은{}원입니다\n커피는 총{}개 주문가능합니다".format(balance,pos_num))
#             elif stuff== 2 and money >= 700:
#                 stuff =700
#                 pos_num=money//stuff
#                 balance =money-stuff
#                 print("음류수가 주문되었습니다.잔액은{}원입니다\n음류수는 총{}개 주문가능합니다".format(balance,pos_num))
#             elif stuff==3 and money >= 930:
#                 stuff=930
#                 balance =money//stuff
#                 pos_num=money-stuff
#                 print("콜라가 주문되었습니다.잔액은{}원입니다\n콜라는 총{}개 주문가능합니다".format(balance,pos_num))
#             else:
#                 print("주문하신 상품이 없거나 금액이 모자릅니다")


# idx =0
# prices =[500,700,930]
# money = int(input("돈:"))
# while idx <= len(prices):
#  price =prices[idx]
#  print(money//price)
#  print(money%price)
#  idx +=1
                    

# while 반복문을 사용해서
# scores 리스트에 시험 점수 5개를
# 정수형으로 입력받으세요


# scores=[]
# n=1
# while n <10:
#      print(2*n)
#      n +=1

# print(scores)

# while 반복문을 사용하여 
# 구구단 2단을 출력하세요.

for i in range(10):
        print(2*i)

