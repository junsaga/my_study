


while True:
            print("#가격:1.양념:11000 2.후라이드:10000,3.엣날통닭:8000")
            print("#종류:1.양념 2.후라이드 3.옛날통닭")
            list=["양념치킨","후라이드치킨","옛날통닭"]
            
            chicken=int(input("치킨 종류>"))
            money = int(input("금액>"))
            if chicken==1 and money >11000:
                양념치킨 =11000
                balance =money-양념치킨
                print("양념치킨이 주문되었습니다.잔액은{}원입니다\n".format(balance))
            elif chicken== 2 and money >10000:
                후라이드치킨 =11000
                balance =money-후라이드치킨
                print("후라이드가 주문되었습니다.잔액은{}원입니다\n".format(balance))
            elif chicken== 3 and money >8000:
                옛날통닭=8000
                balance =money-옛날통닭
                print("옛날 통닭 주문되었습니다.잔액은{}원입니다\n".format(balance))
            else:
                print("주문하신 상품이 없거나 금액이 모자릅니다")
                    
                    

