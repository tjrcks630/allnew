price = 2000
coffee = 5

#매장 커피 현황
print("우리 매장에 커피는 {} 잔 있습니다." .format(coffee))

#자판기 입금 관련
money = int(input("돈을 넣어주세요 : "))
print("{} 원을 입금하셨습니다." .format(money))

#커피 수량 입력
amount = int(input("커피 수량을 입력하세요 : "))
print("{} 잔을 구매하셨습니다. " .format(amount))

#커피 판매 및 거스름 돈
change = money - price
print("거스름돈은 {}원이며, 커피 {}잔을 판매합니다." .format(change, 1))

print("남은 커피의 양은 {} 잔 입니다.\n".format(coffee-1))

