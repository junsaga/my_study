# 모듈
# 함수, 변수, 클래스 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용
# import 명령어로 불러옴
"""
import 모듈이름
"""

# import my_module
# my_module.add(1,2)
# my_module.sub(1,2)
"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import *
"""

# from my_module import add,sub
# add(1,2)
# sub(1,2)

# from my_module import *
# add(1,2)
# sub(1,2)

from  MyCalculator import MyCalculator1
my_calculator = MyCalculator1(10,2)
my_calculator.div(10,2)

# class ZeroCalculator(MyCalculator1):
#         def div(self, n1,n2):
#             if n2 == 0:
#                 print("0으로 나눌 수 없습니다")
#             else:
#                 print(f"{n1}/{n2} ={n1/n2}")
# zeroCalculator = ZeroCalculator()
# zeroCalculator.div(10,0)