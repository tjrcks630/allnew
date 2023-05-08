f = open("out.txt", "w")
f.write("This file is %s \n" % ("out.txt"))
f.write("End of file")
f.close()
#File Write를 통해서 입력


f = open("out.txt", "r")
line = 1
while line:
    line = f.readline()
    print(line)
f.close()
#다시ㅔ 위에 코드에서 작성한File 출력