f = open("test.txt")
line = 1;
while line:
    line =  f.readline()
    print(line)
f.close()
#1번 Line에서 Open으로 test.txt 파일을 열어주니까 닫아주는 Method Close 사용