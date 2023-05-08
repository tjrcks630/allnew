n = 0

while True :
    n += 1
    # n은 1씩증가

    if n > 10:
        break
    #2로 나눠서 나머지가 0이면 출력
    if (n % 2) != 0:
        continue
print(n)
