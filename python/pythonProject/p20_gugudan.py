while True:
    i = input("input the number(q : Quit) : ")

    if i == 'q':
        break

    #Data Type 한번에 Casting
    i = int(i)
    
    if (i < 2 or i > 9):
        print("input number range 2~9!!")
        continue
    else:
        for j in range(1, 10):
            print(f'{i} x {j} = {i * j}')



#내가 짠 코드 ㅠㅠ
# while True:
#     i = input("input the number(q : Quit) : ")
#
#     if i == 'q':
#         break
#
#     elif int(i) < 2 or int(i) > 9:
#         print("input number range 2~9!!")
#
#     else:
#         for j in range(1, 10):
#             print(f'{i} x {j} = {int(i) * j}')


