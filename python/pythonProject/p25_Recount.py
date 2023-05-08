import p25_timer


timer = p25_timer.counter2()
counter = 0
# sum = 0

#For문 예시
for i in range(1,101):
    if i % 7 == 0:
        print(timer())

print(timer())

# #While문 예시
# while True:
#     sum += 7
#     if sum > 100:
#         break
#     counter = timer()
# print(timer())
