salary = int(input("월급을 입력하세요 : "))
income = 0
tax = 0

if salary >= 500:
    income = 12 * salary
else:
    income = 13 * salary


if income >= 10000:
    tax = 0.2 * income

elif income >= 7000:
    tax = 0.15 * income

elif income >= 5000:
    tax = 0.12 * income

elif income >= 1000:
    tax = 0.1 * income

else:
    tax = 0

print("월급 : {}" .format(salary))
print("연봉 : {}" .format(income))
print("세금 : {}" .format(tax))